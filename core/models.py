from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField
from decimal import Decimal

# Constants
CATEGORY_CHOICES = [
    ('P', 'Phones'),
    ('C', 'Cases'),
    ('RP', 'Replacement Parts'),
]


LABEL_CHOICES = [
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
]

ADDRESS_CHOICES = [
    ('B', 'Billing'),
    ('S', 'Shipping'),
]

# Models
class Category(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(default="default_category.jpg", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug': self.slug})

from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='items/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return Decimal(str(self.quantity)) * Decimal(str(self.item.price))

    def get_total_discount_item_price(self):
        if self.item.discount_price:
            return Decimal(str(self.quantity)) * Decimal(str(self.item.discount_price))
        return Decimal(0)

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = Decimal(0)
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100, blank=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.street_address}"


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


# Signals
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


def pre_save_slug_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_slug_receiver, sender=Category)
pre_save.connect(pre_save_slug_receiver, sender=Item)
