from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from restaurant.models import RestaurantInfo,MenuCategory,FoodMenu, BusinessHours, FoodCategory

def index(request):
    return render(request, 'restaurant/index.html', {})

def menu(request):
	menu_cats = MenuCategory.objects.all()
	context = {'menu_cats': menu_cats}
	return render(request, 'restaurant/menu.html', context)

def menu_cat(request, menu_cat_name):
	menu_cat = get_object_or_404(MenuCategory, name=menu_cat_name)
	food_menu_list = FoodMenu.objects.filter(menu_cat = menu_cat).order_by('food_cat')

	menu_dict = {}
	
	for food_menu in food_menu_list:
		if food_menu.food_cat not in menu_dict:
			menu_dict[food_menu.food_cat] = [food_menu]
		else:
			menu_dict[food_menu.food_cat].append(food_menu)

	context = {'menu_cat': menu_cat, 'menu_dict' : menu_dict}
	return render(request, 'restaurant/menu_cat.html', context)

def about_us(request):
	context = {}
	return render(request, 'restaurant/about_us.html', context)