from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
# Create your views here.

class ShowAllProfilesView(ListView):
    '''Shows how the layout of mini fb will be.'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "mini_fb"

class ShowProfilePageView(DetailView):
    ''''''
