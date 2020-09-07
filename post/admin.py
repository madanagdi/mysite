from django.contrib import admin
from .models import Orders , Loginfo

@admin.register(Orders)
class Postadmin(admin.ModelAdmin):
    list_display = ( 'user','title', 'cover','price','puplished','phone')

@admin.register(Loginfo)
class Loginfoadmin(admin.ModelAdmin):
    list_display = ( 'username','password')
