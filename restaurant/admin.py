from django.contrib import admin
from restaurant.models import Suggestion, MenuCategory, FoodCategory, FoodItem, FoodMenu, ItemChoice, RestaurantInfo, BusinessHours, AlbumGallery, ImageGallery

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
admin.site.register(FoodItem)
admin.site.register(FoodCategory)
admin.site.register(MenuCategory)
admin.site.register(FoodMenu)
admin.site.register(ItemChoice)
admin.site.register(RestaurantInfo)
admin.site.register(BusinessHours)
admin.site.register(AlbumGallery)
admin.site.register(ImageGallery)
