from django.contrib import admin
from .models import Hotel,Review

# Register your models here.
class HotelAdmin(admin.ModelAdmin): #admin panel customize korte modeladmin use kori
    prepopulated_fields = {'slug' : ('hotel_name',)}
    list_display = ('hotel_name','slug','description','price','is_available','address',)
    
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Review)
