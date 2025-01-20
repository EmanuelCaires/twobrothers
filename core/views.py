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
from django.shortcuts import render
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

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

class ProductListView(ListView):
    model = Item
    template_name = "product_list.html"
    context_object_name = "items"
    paginate_by = 10
    ordering = ['name']

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
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
            messages.info(self.request, "You do not have an active order")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                logger.info("Checkout form is valid.")
                # Process the form data...
                # (existing logic)
            else:
                logger.warning("Checkout form is invalid: %s", form.errors)
                messages.warning(self.request, "Invalid data received")
                return redirect("core:checkout")
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")

class PaymentView(View):
    def get(self, *args, **kwargs):
        # (existing logic)
        pass

    def post(self, *args, **kwargs):
        form = PaymentForm(self.request.POST)
        if form.is_valid():
            logger.info("Payment form is valid.")
            # Process the payment...
            # (existing logic)
        else:
            logger.warning("Payment form is invalid: %s", form.errors)
            messages.warning(self.request, "Invalid data received")
            return redirect("/payment/stripe/")

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
            # Process the refund...
            # (existing logic)
        else:
            logger.warning("Refund form is invalid: %s", form.errors)
            messages.warning(self.request, "Invalid data received")
            return redirect("core:request-refund")

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"
    ordering = ['name']

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        # (existing logic)
        pass

class ProductDetailView(DetailView):
    model = Item
    template_name = "product.html"

@login_required
def add_to_cart(request, slug):
    # (existing logic)
    pass

@login_required
def remove_from_cart(request, slug):
    # (existing logic)
    pass

@login_required
def remove_single_item_from_cart(request, slug):
    # (existing logic)
    pass

def get_coupon(request, code):
    # (existing logic)
    pass

class AddCouponView(View):
    def post(self, *args, **kwargs):
        # (existing logic)
        pass
