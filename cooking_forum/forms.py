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