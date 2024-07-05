# orders/admin.py
from django.contrib import admin
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'order_date', 'status', 'total_price']
    search_fields = ['id', 'customer_name', 'customer_email']
    list_filter = ['status', 'order_date']
    filter_horizontal = ['products']  # Allows selection of multiple products
    readonly_fields = ['order_date', 'total_price']

    fieldsets = (
        (None, {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'status', 'payment_method', 'payment_status')
        }),
        ('Shipping Address', {
            'fields': ('shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip', 'shipping_country')
        }),
        ('Products and Total', {
            'fields': ('products', 'total_price')
        }),
        ('Order Info', {
            'fields': ('order_date',)
        }),
    )

admin.site.register(Orders, OrdersAdmin)
