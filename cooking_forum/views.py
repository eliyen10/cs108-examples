from django.views.generic.edit import UpdateView
from cooking_forum.forms import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Person
import random
from django.urls import reverse
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

class PersonPageView(DetailView):
    '''Shows list of recipes for a person'''
    model = Person
    template_name = "cooking_forum/person.html"
    context_object_name = "person"

class UserPageView(ListView):
    '''Shows a list of Users'''
    model = Person
    template_name = "cooking_forum/person_list.html"
    context_object_name = "persons"

class CreateUserView(CreateView):
    '''Add a new recipe to the database through a form'''
    model = Person
    form_class = CreateUserForm
    template_name = "cooking_forum/create_user_form.html"

class CreateCommentView(CreateView):
    '''Add a comment to a recipe'''
    model = Comment
    form_class = CreateCommentForm
    template_name = "cooking_forum/create_comment_form.html"

class SearchView(ListView):
    '''Home page of the cooking forum'''

    model = Recipe
    template_name = "cooking_forum/search.html"
    context_object_name = "recipes"

    def get_queryset(self):
        '''Return a query set of quote objects'''

        if 'search_recipe' in self.request.GET:
            search_recipe = self.request.GET['search_recipe']

            return Recipe.objects.filter(recipe_name__contains=search_recipe)

        return None

class DeleteRecipeView(DeleteView):
    '''Delete an existing recipe'''
    model = Recipe
    template_name = "cooking_forum/delete_recipe.html"

    def get_success_url(self):
        '''return to the origninal pge where you deleted the quote'''
        
        pk = self.kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=pk).first()

        person = recipe.person
        return reverse('person', kwargs={'pk':person.pk})