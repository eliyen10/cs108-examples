from django.shortcuts import render
from django.views.generic import ListView
from .models import User
# Create your views here.

class HomePageView(ListView):
    '''Home page of the cooking forum'''
    model = User
    template = "cooking_forum/home.html"
    context_object_name = "users"