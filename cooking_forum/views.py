from cooking_forum.forms import CreateRecipeForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User, Person
from .forms import CreateRecipeForm
# Create your views here.

class HomePageView(ListView):
    '''Home page of the cooking forum'''

    model = User
    template_name = "cooking_forum/home.html"
    context_object_name = "users"

class RecipePageView(DetailView):
    '''Display a single recipe'''
    model = User
    template_name = "cooking_forum/forum.html"
    context_object_name = "user"

class CreateRecipeView(CreateView):
    '''Add a new recipe to the database through a form'''
    model = User
    form_class = CreateRecipeForm
    template_name = "cooking_forum/create_quote_form.html"
