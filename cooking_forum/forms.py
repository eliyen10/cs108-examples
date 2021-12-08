# forms.py

from django import forms
from .models import *

class CreateRecipeForm(forms.ModelForm):
    '''Gives a form to input a new recipe into the system.'''

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'ingredients', 'person', 'image_url'] 

class UpdateRecipeForm(forms.ModelForm):
    '''Updates an existing recipe.'''

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'ingredients', 'person', 'image_url'] 

class CreateUserForm(forms.ModelForm):
    '''Gives a form to input a new user into the system.'''

    class Meta:
        model = Person
        fields = ['name'] 

class CreateCommentForm(forms.ModelForm):
    '''A form to add a comment to a recipe'''

    class Meta:
        model = Comment
        fields = ['person', 'recipe_comment', 'recipe'] 