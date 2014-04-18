from restaurant.models import RestaurantInfo, BusinessHours, MenuCategory
from django.http import Http404
def restaurant_info(request):
	try: 
		restaurant_obj = RestaurantInfo.objects.all()[:1].get()
	except RestaurantInfo.DoesNotExist:
		raise Http404
	business_hours_list = BusinessHours.objects.all()
	return {'restaurant_obj': restaurant_obj, 'business_hours_list' : business_hours_list}

def menu_category(request):
	menu_cats = MenuCategory.objects.all()
	return {'menu_cats': menu_cats}

