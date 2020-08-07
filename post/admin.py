from django.contrib import admin
from .models import Orders , Login

@admin.register(Orders)
class Postadmin(admin.ModelAdmin):
    list_display = ( 'user','title', 'cover','price','puplished','phone')

# Register your models here.
@admin.register(Login) 
class Loginadmin(admin.ModelAdmin):
    list_display = ('email','passwod')