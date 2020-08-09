from django.contrib import admin
from .models import Orders 

@admin.register(Orders)
class Postadmin(admin.ModelAdmin):
    list_display = ( 'user','title', 'cover','price','puplished','phone')
