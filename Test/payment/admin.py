from django.contrib import admin
from .models import Item,Order
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
	list_display = ['name','price','description']
	list_filter  = ['price']


	
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)