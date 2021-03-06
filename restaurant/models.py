from django.db import models
import datetime
from django.utils import timezone
from decimal import Decimal
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
import hashlib

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

class RestaurantInfo(models.Model):
	"""
	Model storing basic information of the restaurant
	"""
	name = models.CharField(max_length=50)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	fax = models.CharField(max_length=20, null=True, blank=True)
	street = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	zipcode = models.IntegerField(null=True, blank=True)
	about_us = models.TextField(null=True, blank=True)
	logo = models.ImageField(upload_to = 'images/RestaurantInfo/', blank=True)
	def __unicode__(self):
		return self.name

class BusinessHours(models.Model):
	"""
	Model to store business hours of the restaurant
	"""
	day = models.IntegerField(choices=DAYS_OF_WEEK)
	open_time = models.TimeField('open time')
	close_time = models.TimeField('close time')

	def contain_curr_time(self, curr_date_time):
		"""
		Function to return whether the input curr_date_time is in the time/date represeted by the tuple.
		"""
		#curr_date_time = timezone.localtime(timezone.now())
		if(self.day == curr_date_time.weekday()):
			return ((self.open_time <= curr_date_time.time()) and (curr_date_time.time() <= self.close_time))
		return False

	def __unicode__(self):
		return "%s" % self.get_day_display()

class Suggestion(models.Model):
	"""
	Model to store suggestion from customer
	"""
	name = models.CharField(max_length=50)
	email = models.EmailField()
	post_date = models.DateTimeField('date posted', auto_now = True)
	content = models.TextField()   
	def __unicode__(self):
		return u"%s" % self.id

class MenuCategory(models.Model):
	"""
	Model to store categories of menu (e.g, dinner, lunch, etc.)
	"""
	name = models.CharField(max_length=50, unique = True)
	description = models.CharField(max_length=255, null=True, blank=True)
	start_day = models.IntegerField('start serving day', choices=DAYS_OF_WEEK, null=True, blank=True)
	end_day = models.IntegerField('end serving day', choices=DAYS_OF_WEEK, null=True, blank=True)
	start_time = models.TimeField('start serving time', null=True, blank=True)
	end_time = models.TimeField('end serving time', null=True, blank=True)

	def contain_curr_time(self, curr_date_time):
		"""
		Function to return whether the input curr_date_time is in the time/date represeted by the tuple.
		"""
		if(self.start_day <= curr_date_time.weekday() and curr_date_time.weekday() <= self.end_day):
			return ((self.start_time <= curr_date_time.time()) and (curr_date_time.time() <= self.end_time))
		return False

	def __unicode__(self):
		return self.name

class FoodCategory(models.Model):
	"""
	Model to store categories of food (e.g, noodle, sandwich, etc.)
	"""
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name

class FoodItem(models.Model):
	"""
	Model to store food item and its detail
	"""
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to = 'images/FoodItem/', blank=True)
	def __unicode__(self):
		return self.name

class ItemChoice(models.Model):
	"""
	Model to store choices of food item, having food item as foreign key
	"""
	name = models.CharField(max_length=50)
	food_item = models.ForeignKey(FoodItem)
	price_add = models.FloatField()
	def __unicode__(self):
		return u"%s [%s]" % (self.food_item, self.get_name_display()) 	

class FoodMenu(models.Model):
	"""
	Model to represent menu of a restaurant where each tuple refer to a food item in a food category in a menu category
	"""
	food_item = models.ForeignKey(FoodItem)
	food_cat = models.ForeignKey(FoodCategory)	
	menu_cat = models.ForeignKey(MenuCategory)
	price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
	def __unicode__(self):
		return self.food_item.name + " | " + self.menu_cat.name

class AlbumGallery(models.Model):
	"""
	Model to represent gallery album
	"""
	name = models.CharField(max_length=50, default = "untitled")
	description = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return self.name
        
class ImageGallery(models.Model):
	"""
	Model to represent gallery image
	"""
	name = models.CharField(max_length=50,  default = "untitled")
	image = models.ImageField(upload_to = 'images/ImageGallery')
	albums = models.ManyToManyField(AlbumGallery)
	def __unicode__(self):
		return self.name

class LikeFoodMenu(models.Model):
	"""
	Model to represent customer liking food menu
	"""
	customer = models.ForeignKey(User)
	food_menu = models.ForeignKey(FoodMenu)


	