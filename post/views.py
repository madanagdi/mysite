from django.views.generic import ListView
from django.shortcuts import render 
from django.http import HttpResponse 
from .models import  Orders , Loginfo
from datetime import date



class HomePageView(ListView):
    model = Orders
    template_name = 'home.html'


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Loginfo(username = username , password= password)
    data.save()
    return render (request , 'login.html',{})


