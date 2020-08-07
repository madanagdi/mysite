from django.views.generic import ListView
from .models import Orders
from django.shortcuts import render
from django.http import HttpResponse 
from .models import  Orders , Login
from datetime import date



class HomePageView(ListView):
    model = Orders
    template_name = 'home.html'

class LogIn(ListView):
    model = Login
    template_name = 'login.html'





def loginpage(request): 

    name = ['nigo','mase']
    return render (request, 'login.html',{"name":name})
    
