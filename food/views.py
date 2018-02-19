from django.shortcuts import render
from . import views
from .models import Category, Item


def index(request):
	categories = Category.objects.all()
	items = Item.objects.all()
	return render(request, 'food/index.html', {'categories': categories, 'items': items})