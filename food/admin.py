from django.contrib import admin
from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
	pass


class	ItemAdmin(admin.ModelAdmin):
	list_display = ['item', 'category',]
	search_fields = ['item',]
	list_editable = ['category',]
	list_display_links = ['item',]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)