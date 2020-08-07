
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', LogIn.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    

]
