# forms.py

from django import forms
from .models import *

class CreateRecipeForm(forms.ModelForm):
    '''Gives a form to input a new recipe into the system.'''

    class Meta:
        model = User
        fields = ['recipes', 'username']