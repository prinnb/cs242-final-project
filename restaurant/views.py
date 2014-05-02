from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from restaurant.models import RestaurantInfo,MenuCategory,FoodMenu, BusinessHours, FoodCategory, AlbumGallery, ImageGallery, LikeFoodMenu
from forms import SuggestionForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

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
	is_signed_in = request.user.is_authenticated()

	for food_menu in food_menu_list:
		curr_like_list = LikeFoodMenu.objects.filter(food_menu = food_menu)
		is_like = ''
		num_other_like = curr_like_list.count()

		if is_signed_in and curr_like_list.filter(customer = request.user):
			is_like = True
			num_other_like = curr_like_list.count() - 1
		elif is_signed_in and not curr_like_list.filter(customer = request.user):
			is_like = False
		else:
			is_like = False

		if food_menu.food_cat not in menu_dict:
			menu_dict[food_menu.food_cat] = [(food_menu, num_other_like, is_like, request.user.id)]
		else:
			menu_dict[food_menu.food_cat].append((food_menu, num_other_like, is_like, request.user.id))

	context = {'menu_cat': menu_cat, 'menu_dict' : menu_dict}
	return render(request, 'restaurant/menu_cat.html', context)

def about_us(request):
	context = {}
	return render(request, 'restaurant/about_us.html', context)

def suggestion(request):
	if request.method == 'POST': 
		form = SuggestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/restaurant/') 

	elif request.user.is_authenticated():
		#automatically fill out name and email for logged in user
		form = SuggestionForm(initial = {'name': request.user.username, 'email': request.user.email})
	else:
		form = SuggestionForm()
	context = {}
	context.update(csrf(request))
	context['form'] = form
	return render(request, 'restaurant/suggestion.html', context)

def login_index(request):
    return render_to_response("restaurant/login_index.html", RequestContext(request))

def gallery(request):
	albums = AlbumGallery.objects.all()
	context = {'albums': albums}
	return render(request, 'restaurant/gallery.html', context)

def album(request, album_name):
	album = get_object_or_404(AlbumGallery, name=album_name)
	images = album.imagegallery_set.all()
	context = {'images': images}

	return render(request, 'restaurant/album.html', context)

def food_menu_like(request, food_menu_id):
	if request.method == 'POST':
		num_other_like = request.POST['num_other_like']
		if request.user.is_authenticated() and food_menu_id:
			curr_food_menu = FoodMenu.objects.get(id = int(food_menu_id))
			(obj, created) = LikeFoodMenu.objects.get_or_create(customer = request.user, food_menu = curr_food_menu)
			if created == False:
				obj.delete()
				return render(request, 'ajax_like_count.html' , {'is_like' : False, 'num_other_like' : int(num_other_like)})
			return render(request, 'ajax_like_count.html' , {'is_like' : True, 'num_other_like' : int(num_other_like)})
	return HttpResponseRedirect('/restaurant/')

def login_redirect(request):
	return render(request, 'restaurant/login_redirect.html', {})

def logout_redirect(request):
	return render(request, 'restaurant/logout_redirect.html', {})

