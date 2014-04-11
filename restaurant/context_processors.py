from restaurant.models import RestaurantInfo, BusinessHours

def restaurant_info(request):
    restaurant_obj = RestaurantInfo.objects.all()[:1].get()
    business_hours_list = BusinessHours.objects.all()
    return {'restaurant_obj': restaurant_obj, 'business_hours_list' : business_hours_list}

