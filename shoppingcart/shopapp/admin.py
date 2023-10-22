from django.contrib import admin
from . models import Category,Product

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = { 'slug':('name',)}
admin.site.register(Category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['name','category','price','available','stock','created','updated','image']
    list_editable = ['price','available','stock']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Product,Productadmin)