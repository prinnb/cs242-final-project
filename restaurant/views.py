from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from restaurant.models import RestaurantInfo,MenuCategory,FoodMenu, BusinessHours

def index(request):
    return render(request, 'restaurant/index.html', {})

def menu(request):
	menu_cats = MenuCategory.objects.all()
	context = {'menu_cats': menu_cats}
	return render(request, 'restaurant/menu.html', context)

def menu_cat(request, menu_cat_id):
	menu_cat = get_object_or_404(MenuCategory, pk=menu_cat_id)
	food_menu_list = FoodMenu.objects.filter(menu_cat = menu_cat)
	context = {'menu_cat': menu_cat, 'food_menu_list' : food_menu_list}
	return render(request, 'restaurant/menu_cat.html', context)