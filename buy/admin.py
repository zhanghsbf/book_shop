from django.contrib import admin
from .models import *

class ItemInline(admin.StackedInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
	list_display = ['buyer', 'total', 'generate_date']
	inlines = [ItemInline]

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['seller', 'order', 'status', 'post', 'price']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
