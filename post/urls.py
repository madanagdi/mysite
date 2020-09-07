
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('login/', views.login, name='login'),
    

]
