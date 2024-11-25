from django.urls import path
from .views import (
    PhonePartListView, PhoneCaseListView, PhoneCasePartListView,
    phone_part_detail, phone_case_detail, phone_case_part_detail,
    ItemDetailView, CheckoutView, HomeView, OrderSummaryView,
    add_to_cart, remove_from_cart, remove_single_item_from_cart,
    PaymentView, AddCouponView, RequestRefundView,
    ReplacementPartsListView, ReplacementPartDetailView
)

app_name = 'core'

urlpatterns = [
    # New URLs for the three main categories
    path('phone-parts/', PhonePartListView.as_view(), name='phone-parts'),
    path('phone-cases/', PhoneCaseListView.as_view(), name='phone-cases'),
    path('phone-case-parts/', PhoneCasePartListView.as_view(), name='phone-case-parts'),
    
    # Detail views for individual items in each category
    path('phone-part/<slug>/', phone_part_detail, name='phone-part-detail'),
    path('phone-case/<slug>/', phone_case_detail, name='phone-case-detail'),
    path('phone-case-part/<slug>/', phone_case_part_detail, name='phone-case-part-detail'),
    path('replacement-parts/', ReplacementPartsListView.as_view(), name='replacement_parts_list'),
    path('replacement-part/<int:pk>/', ReplacementPartDetailView.as_view(), name='replacement_part_detail'),

    # Existing URLs for checkout, cart, etc.
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    
 
    
]

