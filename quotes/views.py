from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

# Create your views here.

class HomePageView(ListView):
    '''Show list of quotes'''

    model = Quote
    template_name = "quotes/home.html"
    context_object_name = "quotes"
