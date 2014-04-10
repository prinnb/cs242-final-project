from django.db import models
import datetime
from django.utils import timezone

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
	name = models.CharField(max_length=50)
	about_us = models.TextField(null=True, blank=True)

	logo = models.ImageField(upload_to = 'images/RestaurantInfo/', blank=True)
	def __unicode__(self):
		return self.name

class BusinessHours(models.Model):
	day = models.IntegerField(choices=DAYS_OF_WEEK)
	open_time = models.TimeField('open time')
	close_time = models.TimeField('close time')

	def contain_curr_time(self, curr_date_time):
		#curr_date_time = timezone.localtime(timezone.now())
		if(self.day == curr_date_time.weekday()):
			return ((self.open_time < curr_date_time.time()) and (curr_date_time.time() < self.close_time))
		return False

	def __unicode__(self):
		return "%s" % self.get_day_display()

class Suggestion(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    post_date = models.DateTimeField('date posted')
    content = models.TextField()   
    def __unicode__(self):
		return u"%s" % self.id

class MenuCategory(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	start_day = models.IntegerField('start serving day', choices=DAYS_OF_WEEK, blank=True)
	end_day = models.IntegerField('end serving day', choices=DAYS_OF_WEEK, blank=True)
	start_time = models.TimeField('start serving time', null=True, blank=True)
	end_time = models.TimeField('end serving time', null=True, blank=True)

	def contain_curr_time(self, curr_date_time):
		if(self.start_day <= curr_date_time.weekday() and curr_date_time.weekday() <= self.end_day):
			return ((self.start_time < curr_date_time.time()) and (curr_date_time.time() < self.end_time))
		return False

	def __unicode__(self):
		return self.title

class FoodCategory(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class FoodDetail(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	image = models.ImageField(upload_to = 'images/FoodItem/', blank=True)
	def __unicode__(self):
		return self.name

class FoodChoice(models.Model):
	FOOD_CHOICES = (
	    ('0', 'Regular'),
	    ('1', 'Combo'),
	)
	name = models.CharField(max_length=1, choices=FOOD_CHOICES)
	food_detail = models.ForeignKey(FoodDetail)
	price_add = models.FloatField()
	def __unicode__(self):
		return u"%s [%s]" % (self.food_item, self.get_name_display()) 	

class FoodMenu(models.Model):
	food_detail = models.ForeignKey(FoodDetail)
	food_cat = models.ForeignKey(FoodCategory)	
	menu_cat = models.ForeignKey(MenuCategory)
	price = models.FloatField()
	def __unicode__(self):
		return self.food_item.name + " | " + self.menu_cat.title
	