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
    AllProductsView,
    all_products,
    phones,  # Ensure this view is defined
    cases,   # Ensure this view is defined
    replacement_parts,  # Ensure this view is defined
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
    path('products/', all_products, name='all_products'),  # Products list
    
    # Cart actions
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),

    # Payment and Refunds
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    # Coupon management
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),

    # Additional categories
    path('phones/', phones, name='phones'),
    path('cases/', cases, name='cases'),
    path('replacement-parts/', replacement_parts, name='replacement_parts'),
]
