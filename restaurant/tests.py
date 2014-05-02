import datetime
from django.utils import timezone
from django.test import TestCase
from restaurant.models import Suggestion, MenuCategory, FoodCategory, FoodItem, FoodMenu, ItemChoice, RestaurantInfo, BusinessHours, AlbumGallery, ImageGallery
from django.core.urlresolvers import reverse
from forms import SuggestionForm

class RestaurantTests(TestCase):

	def test_basic_field(self):
		"""
		Test basic input to email, text, char, and integer field, using RestaurantInfo.
		"""
		test_rest_name = "Prinn Restauarant"
		test_rest_about_us = "Welcome to our restaurant!!!"
		test_rest_email = "pb@gmail.com"
		test_rest_zipcode = "61801"

		test_rest = RestaurantInfo(name = test_rest_name, about_us = test_rest_about_us, 
						email = test_rest_email, zipcode = test_rest_zipcode)
		self.assertEqual(test_rest.name, test_rest_name)
		self.assertEqual(test_rest.about_us, test_rest_about_us)
		self.assertEqual(test_rest.email, test_rest_email)
		self.assertEqual(test_rest.zipcode, test_rest_zipcode)

 	def test_basic_business_hours(self):
 		"""
		Test input to BusinessHours model which deal with choices and timefield
		"""

		test_bus_hours1 = BusinessHours(day = 4, open_time = datetime.time(9,30), close_time = datetime.time(16,00))
		self.assertEqual(test_bus_hours1.get_day_display(), "Friday")
		self.assertEqual(test_bus_hours1.open_time.hour, 9)
		self.assertEqual(test_bus_hours1.close_time.minute, 0)

	def test_contain_curr_time_bh(self):
		"""
		Test function contain_curr_time in BusinessHours model
		"""
		curr_date_time = datetime.datetime(2014, 4, 9, 15, 55, 52)
		test_bus_hours1 = BusinessHours(day = curr_date_time.weekday(), 
							open_time = datetime.time(9,30), close_time = datetime.time(16,00))
		test_bus_hours2 = BusinessHours(day = curr_date_time.weekday(), 
							open_time = datetime.time(9,30), close_time = datetime.time(15,00))
		test_bus_hours3 = BusinessHours(day = 0, open_time = datetime.time(9,30), close_time = datetime.time(21,00))

		self.assertTrue(test_bus_hours1.contain_curr_time(curr_date_time))
		self.assertFalse(test_bus_hours2.contain_curr_time(curr_date_time))
		self.assertFalse(test_bus_hours3.contain_curr_time(curr_date_time))

	def test_basic_menu_category(self):
 		"""
		Test input to MenuCategory model which deal with choices and timefield
		"""

		test_name = "dinner"
		test_description = "Best Dinner"
		test_menu_category = MenuCategory(name = test_name, description = test_description, start_day = 0, 
								end_day = 6, start_time = datetime.time(16,00), end_time = datetime.time(22,00))
		self.assertEqual(test_menu_category.name, test_name)
		self.assertEqual(test_menu_category.get_end_day_display(), "Sunday")
		self.assertEqual(test_menu_category.start_time.hour, 16)

	def test_contain_curr_time_mc(self):
		"""
		Test function contain_curr_time in MenuCategory model
		"""
		test_menu_category = MenuCategory(name = "dinner", description = "Best Dinner", start_day = 0, 
								end_day = 5, start_time = datetime.time(16,00), end_time = datetime.time(22,00))

		curr_date_time1 = datetime.datetime(2014, 4, 9, 16, 55, 52)
		self.assertTrue(test_menu_category.contain_curr_time(curr_date_time1))

		curr_date_time2 = datetime.datetime(2014, 4, 6, 16, 55, 52)
		self.assertFalse(test_menu_category.contain_curr_time(curr_date_time2))

		curr_date_time3 = datetime.datetime(2014, 4, 9, 15, 55, 52)
		self.assertFalse(test_menu_category.contain_curr_time(curr_date_time3))

	def test_item_choice(self):
		"""
		Test ItemChoice model which deals with foreign key
		"""
		test_item = FoodItem(name = 'pep pizza', description = "with cheese")
		test_choice = ItemChoice(name = 'combo', food_item = test_item, price_add = 1.00)
		self.assertEqual(test_choice.name, 'combo')
		self.assertEqual(test_choice.food_item.name, 'pep pizza')

	def test_food_menu(self):
		"""
		Test FoodMenu model which deals foreign keys
		"""
		test_food_item = FoodItem(name = 'pep pizza', description = "with cheese")
		test_food_cat = FoodCategory(name = 'pizza')
		test_menu_cat = MenuCategory(name = 'lunch')
		test_price = 3.50

		test_food_menu = FoodMenu(food_item = test_food_item, 
		food_cat = test_food_cat, menu_cat = test_menu_cat, price = test_price)
		self.assertEqual(test_food_menu.food_item.name, 'pep pizza')
		self.assertEqual(test_food_menu.food_cat.name, 'pizza')
		self.assertEqual(test_food_menu.menu_cat.name, 'lunch')
		self.assertEqual(test_food_menu.price, test_price)


class RestaurantViewTests(TestCase):

	def create_test_restaurant(rest_name):
		"""
		Create a minimal RestaurantInfo object with the input name as its name
		"""
		return RestaurantInfo.objects.create(name = rest_name)

	def create_test_food_item(food_cat_name):
		"""
		Create a minimal FoodItem object with the input name as its name
		"""
		return FoodItem.objects.create(name = food_cat_name)

	def create_test_food_cat(menu_cat_name):
		"""
		Create a minimal FoodCategory object with the input name as its name
		"""
		return FoodCategory.objects.create(name = menu_cat_name)

	def create_test_menu_cat(price):
		"""
		Create a minimal MenuCategory object with the input name as its name
		"""
		return MenuCategory.objects.create(name = price)

	def create_test_food_menu(food_item, food_cat, menu_cat, price):
		"""
		Create a FoodMenu object with the input FoodItem, FoodCategory, MenuCategory, and price
		"""
		return FoodMenu.objects.create(food_item=food_item, food_cat=food_cat, menu_cat = menu_cat, price = price)

	def test_menu_cat_view_with_one_menu_item(self):
		"""
		Test displaying a food menu object in one menu category
		"""
		restaurant = create_test_restaurant("test_rest")
		food_item = create_test_food_item("test_food_item")
		food_cat = create_test_food_cat("test_food_cat")
		menu_cat = create_test_menu_cat("test_menu_cat")

		create_test_food_menu(food_item, food_cat, menu_cat, 4.00)
		response = self.client.get(reverse('menu_cat', args=["test_menu_cat"]))

		self.assertEqual(response.context['menu_cat'].name, 'test_menu_cat' )
		self.assertQuerysetEqual(response.context['menu_dict'][food_cat], ['<FoodMenu: test_food_item | test_menu_cat>'] )

	def test_menu_cat_view_with_two_menu_item(self):
		"""
		Test displaying food menu objects in two different menu categories
		"""
		restaurant = create_test_restaurant("test_rest")
		food_item1 = create_test_food_item("test_food_item1")
		food_cat1 = create_test_food_cat("test_food_cat1")
		menu_cat1 = create_test_menu_cat("test_menu_cat1")

		food_item2 = create_test_food_item("test_food_item2")
		food_cat2 = create_test_food_cat("test_food_cat2")
		menu_cat2 = create_test_menu_cat("test_menu_cat2")

		create_test_food_menu(food_item1, food_cat1, menu_cat1, 4.00)
		create_test_food_menu(food_item2, food_cat2, menu_cat2, 5.00)
		
		response = self.client.get(reverse('menu_cat', args=["test_menu_cat1"]))
		self.assertEqual(response.context['menu_cat'].name, 'test_menu_cat1' )
		self.assertQuerysetEqual(response.context['menu_dict'][food_cat1], ['<FoodMenu: test_food_item1 | test_menu_cat1>'] )
		response = self.client.get(reverse('menu_cat', args=["test_menu_cat2"]))
		self.assertQuerysetEqual(response.context['menu_dict'][food_cat2], ['<FoodMenu: test_food_item2 | test_menu_cat2>'] )

class RestaurantFormTests(TestCase):

    def test_valid_suggestion_form(self):
    	"""
    	Test suggestion form with the valid input
    	"""
        form_data = {'name' : 'test user', 'email' : 'test@gmail.com', 'content' : 'this is a test suggestion.'}
        form = SuggestionForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_invalid_suggestion_form(self):
    	"""
    	Test suggestion form with invalid inputs. 
    	The first one test detecting blank field. The second one test for invalid email.
    	"""
        form_data_blank_name = {'name' : '', 'email' : 'test@gmail.com', 'content' : 'this is a test suggestion.'}
        form = SuggestionForm(data=form_data_blank_name)
        self.assertEqual(form.is_valid(), False)

        form_data_incorrect_email = {'name' : 'test user', 'email' : 'test.com', 'content' : 'this is a test suggestion.'}
        form = SuggestionForm(data=form_data_incorrect_email)
        self.assertEqual(form.is_valid(), False)


