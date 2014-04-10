import datetime
from django.utils import timezone
from django.test import TestCase
from restaurant.models import Suggestion, MenuCategory, FoodCategory, FoodItem, FoodMenu, FoodChoice, RestaurantInfo, BusinessHours


class RestaurantTests(TestCase):

	def test_basic_restaurant_info(self):
		"""
		"""
		test_rest_name = "Prinn Restauarant"
		test_rest_about_us = "Welcome to our restaurant!!!"
		test_rest = RestaurantInfo(name = test_rest_name, about_us = test_rest_about_us)
		self.assertEqual(test_rest.name, test_rest_name)
		self.assertEqual(test_rest.about_us, test_rest_about_us)

	def test_contain_curr_time_bh(self):
		curr_date_time = datetime.datetime(2014, 4, 9, 15, 55, 52)
		test_bus_hours1 = BusinessHours(day = curr_date_time.weekday(), open_time = datetime.time(9,30), close_time = datetime.time(16,00))
		test_bus_hours2 = BusinessHours(day = curr_date_time.weekday(), open_time = datetime.time(9,30), close_time = datetime.time(15,00))
		test_bus_hours3 = BusinessHours(day = 0, open_time = datetime.time(9,30), close_time = datetime.time(21,00))

		self.assertTrue(test_bus_hours1.contain_curr_time(curr_date_time))
		self.assertFalse(test_bus_hours2.contain_curr_time(curr_date_time))
		self.assertFalse(test_bus_hours3.contain_curr_time(curr_date_time))

 	def test_basic_business_hours(self):
		test_bus_hours1 = BusinessHours(day = 4, open_time = datetime.time(9,30), close_time = datetime.time(16,00))
		self.assertEqual(test_bus_hours1.get_day_display(), "Friday")
		self.assertEqual(test_bus_hours1.open_time.hour, 9)
		self.assertEqual(test_bus_hours1.close_time.minute, 0)

	#def test_basic_menu_category(self):
		


	def test_contain_curr_time_mc(self):
		curr_date_time = datetime.datetime(2014, 4, 9, 15, 55, 52)
		test_menu_category = MenuCategory(title = "dinner", description = "Best Dinner", 
								start_day = 0, end_day = 6, start_time = datetime.time(16,00), end_time = datetime.time(22,00))
		self.assertTrue(test_bus_hours1.contain_curr_time(curr_date_time))

