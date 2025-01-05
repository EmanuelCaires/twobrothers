from django.contrib import admin
from .models import (
    Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, Category
)


# Action for updating refund status
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Update orders to refund granted'


# Admin customization for Order
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = [
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted'
    ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


# Admin customization for Address
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user__username', 'street_address', 'apartment_address', 'zip']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'slug']
    list_filter = ['category']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'description', 'price', 'discount_price', 'image', 'category', 'slug']
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['category'].required = False
        form.base_fields['category'].empty_label = "No category"
        return form
    
    def save_model(self, request, obj, form, change):
        if not obj.category:
            obj.category = None
        super().save_model(request, obj, form, change)

# Register models with custom admin configurations
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
