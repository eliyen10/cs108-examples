from django.urls import path
from .views import * # HomePageView, QuotePageView, RandomQuotePageView, PersonPageView


urlpatterns = [
    # map the URL (empty string) to the view
    path('all', HomePageView.as_view(), name='all_quotes'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
    path('', RandomQuotePageView.as_view(), name='random'),  # show one quote at random 
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), # show one quote
]