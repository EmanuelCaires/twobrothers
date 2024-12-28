from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    product_list,  # Updated view for handling products dynamically by category
)

app_name = 'core'

urlpatterns = [
    # Homepage
    path('', HomeView.as_view(), name='home'),

    # Checkout and Order Summary
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),

    # Product-related views
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('products/', product_list, name='product_list'),  # All products
    path('products/<slug:category_slug>/', product_list, name='product_list_by_category'),  # Filter by category

    # Cart actions
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),

    # Payment and Refunds
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    # Coupon management
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
]
