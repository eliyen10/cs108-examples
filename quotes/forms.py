from django import forms
from .models import Quote


class CreateQuoteForm(forms.ModelForm):
    '''A form to create a new quote object'''


    class Meta:
        ''''''
        model = Quote
        fields = ['text, person']