from django.views.generic.edit import UpdateView
from cooking_forum.forms import CreateRecipeForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Recipe, Person
import random
from .forms import CreateRecipeForm, UpdateRecipeForm
# Create your views here.

class HomePageView(ListView):
    '''Home page of the cooking forum'''

    model = Recipe
    template_name = "cooking_forum/home.html"
    context_object_name = "recipes"

class RandomRecipePageView(DetailView):
    '''Display a single random recipe'''
    model = Recipe
    template_name = "cooking_forum/forum.html"
    context_object_name = "recipe"

    def get_object(self):
        '''Select a random quote and display it using forum.html'''
        recipes = Recipe.objects.all()

        q = random.choice(recipes)

        return q
class RecipePageView(DetailView):
    '''Display a single recipe'''
    model = Recipe
    template_name = "cooking_forum/forum.html"
    context_object_name = "recipe"

class CreateRecipeView(CreateView):
    '''Add a new recipe to the database through a form'''
    model = Recipe
    form_class = CreateRecipeForm
    template_name = "cooking_forum/create_recipe_form.html"

class UpdateRecipeView(UpdateView):
    '''Update an existing recipe'''
    model = Recipe
    form_class = UpdateRecipeForm
    template_name = "cooking_forum/update_recipe_form.html"

class PersonPageView(ListView):
    '''Shows list of recipes for a person'''
    model = Person
    template_name = "cooking_forum/person.html"
    context_object_name = "person"