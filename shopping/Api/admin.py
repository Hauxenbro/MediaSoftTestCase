from django.contrib import admin
from .models import Shops, Street, City
# Register your models here.

@admin.register(Shops)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city', 'street', 'house_number']
    list_display_links = ['id', 'title']
    search_fields = ('title', 'city')
    list_filter = ('city',)

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'city']
    list_display_links = ['title']
    search_fields =  ('title', 'city')
    list_filter = ('city',)

@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['id' ,'title']
    list_display_links = ['title']
    search_fields = ('id', 'title')