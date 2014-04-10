from django.contrib import admin
from restaurant.models import Suggestion, MenuCategory, FoodCategory, FoodDetail, FoodMenu, FoodChoice, RestaurantInfo, BusinessHours

class FoodMenuInline(admin.StackedInline):
    model = FoodMenu
    extra = 0

class FoodItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]
    inlines = [FoodMenuInline]

admin.site.register(Suggestion)
admin.site.register(FoodDetail)
admin.site.register(MenuCategory)
admin.site.register(FoodMenu)
admin.site.register(FoodChoice)
admin.site.register(RestaurantInfo)
admin.site.register(BusinessHours)