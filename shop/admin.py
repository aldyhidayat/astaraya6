from django.contrib import admin

from .models import *

class ArtikelAdmin(admin.ModelAdmin):
	readonly_fields = [
	'slug',
	'published'
	]
	
admin.site.register(Customer)
admin.site.register(Product, ArtikelAdmin)
admin.site.register(Men)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)

