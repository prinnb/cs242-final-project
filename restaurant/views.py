from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from restaurant.models import RestaurantInfo,MenuCategory

def index(request):
    restaurant_obj = RestaurantInfo.objects.all()[:1].get()
    context = {'restaurant_obj': restaurant_obj}
    return render(request, 'restaurant/index.html', context)

def menu(request):
	menu_cats = MenuCategory.objects.all()
	context = {'menu_cats': menu_cats}
	return render(request, 'restaurant/menu.html', context)

def menu_cat(request, menu_cat_id):
	#menu_cats = MenuCategory.objects.all()
	#context = {'menu_cats': menu_cats}
	context = {}
	menu_cat = get_object_or_404(MenuCategory, pk=menu_cat_id)
	#menu_list
	context = {'menu_cat': menu_cat}
	return render(request, 'restaurant/menu_cat.html', context)