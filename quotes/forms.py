from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to create a new Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to create
        fields = ['text', 'person'] # which fields to create

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update an existing Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to create
        fields = ['text', 'person'] # which fields to create