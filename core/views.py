import random
import string
import logging

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile, Category

# Set up logging
logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def phones(request):
    items = Item.objects.filter(
        category__category='P'
    ).order_by('name')
    categories = Category.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'category_title': 'Phones'
    }
    return render(request, 'product_list.html', context)

def cases(request):
    items = Item.objects.filter(
        category__category='C'
    ).order_by('name')
    categories = Category.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'category_title': 'Cases'
    }
    return render(request, 'product_list.html', context)

def replacement_parts(request):
    items = Item.objects.filter(
        category__category='RP'
    ).order_by('name')
    categories = Category.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'category_title': 'Replacement Parts'
    }
    return render(request, 'product_list.html', context)

class ProductListView(ListView):
    model = Item
    template_name = "product_list.html"
    context_object_name = "items"
    paginate_by = 10
    ordering = ['name']

class ProductDetailView(DetailView):
    model = Item
    template_name = "product.html"

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            logger.info("Attempting to retrieve order for checkout")
            order = Order.objects.get(user=self.request.user, ordered=False)
            logger.info(f"Order found: {order.id}")
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            logger.warning("No active order found for checkout")
            messages.info(self.request, "You do not have an active order")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            logger.info("Processing checkout form")
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                logger.info("Checkout form is valid")
                
                use_default_billing = form.cleaned_data.get('use_default_billing')
                
                if use_default_billing:
                    logger.info("Using default billing address")
                    billing_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='B',
                        default=True
                    )
                    if billing_qs.exists():
                        billing_address = billing_qs[0]
                        order.billing_address = billing_address
                        order.save()
                        logger.info(f"Using default billing address for order {order.id}")
                    else:
                        messages.info(self.request, "No default billing address available")
                        return redirect('core:checkout')
                else:
                    logger.info("Creating new billing address")
                    billing_address = Address(
                        user=self.request.user,
                        street_address=form.cleaned_data.get('billing_address'),
                        apartment_address=form.cleaned_data.get('billing_address2'),
                        country=form.cleaned_data.get('billing_country'),
                        zip=form.cleaned_data.get('billing_zip'),
                        address_type='B'
                    )
                    billing_address.save()
                    
                    if form.cleaned_data.get('set_default_billing'):
                        billing_address.default = True
                        billing_address.save()
                        logger.info("Setting as default billing address")
                    
                    order.billing_address = billing_address
                    order.save()
                    logger.info(f"New billing address saved for order {order.id}")
                
                return redirect("core:payment", payment_option="stripe")
            else:
                logger.warning(f"Checkout form invalid: {form.errors}")
                messages.warning(self.request, "Invalid data received")
                return redirect("core:checkout")
        except ObjectDoesNotExist:
            logger.warning("No active order found during checkout")
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")

class PaymentView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if order.billing_address:
                context = {
                    'order': order,
                    'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
                }
                logger.info(f"Rendering payment page for order {order.id}")
                return render(self.request, "payment.html", context)
            else:
                logger.warning("No billing address found")
                messages.warning(self.request, "Please add a billing address")
                return redirect("core:checkout")
        except ObjectDoesNotExist:
            logger.warning("No active order found for payment")
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")

    def post(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            token = self.request.POST.get('stripeToken')
            
            logger.info(f"Processing payment for order {order.id}")
            if not token:
                logger.warning("No payment token received")
                messages.warning(self.request, "No payment token received")
                return redirect("core:payment")

            amount = int(order.get_total() * 100)
            
            try:
                logger.info(f"Creating Stripe charge for {amount} cents")
                charge = stripe.Charge.create(
                    amount=amount,
                    currency="usd",
                    source=token,
                    description=f"Payment for order {order.id}"
                )
                logger.info(f"Stripe charge successful: {charge['id']}")

                payment = Payment()
                payment.stripe_charge_id = charge['id']
                payment.user = self.request.user
                payment.amount = order.get_total()
                payment.save()
                logger.info(f"Payment record created: {payment.id}")

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                order.save()
                logger.info(f"Order {order.id} marked as paid")

                messages.success(self.request, "Payment was successful!")
                return redirect("core:order-summary")

            except stripe.error.CardError as e:
                logger.error(f"Card error: {str(e)}")
                messages.warning(self.request, f"Card Error: {e.error.message}")
                return redirect("core:payment")
            except stripe.error.InvalidRequestError as e:
                logger.error(f"Invalid request error: {str(e)}")
                messages.warning(self.request, "Invalid parameters")
                return redirect("core:payment")
            except Exception as e:
                logger.error(f"Unexpected error during payment: {str(e)}")
                messages.warning(self.request, "Something went wrong. Please try again")
                return redirect("core:payment")

        except ObjectDoesNotExist:
            logger.warning("No active order found during payment processing")
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order': order
            }
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form
        }
        return render(self.request, "request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            logger.info("Refund form is valid.")
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your refund request was received")
                return redirect("core:request-refund")
            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist")
                return redirect("core:request-refund")
        else:
            logger.warning("Refund form is invalid: %s", form.errors)
            messages.warning(self.request, "Invalid data received")
            return redirect("core:request-refund")

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "Item was added to your cart.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item was added to your cart.")
    return redirect("core:order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "Item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                order.items.remove(order_item)
                order_item.delete()
                messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("core:checkout")

class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("core:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("core:checkout")
