from django.urls import path
from .views import CreateRecipeView, HomePageView, RecipePageView # our view class definition 

urlpatterns = [
    path('all', HomePageView.as_view(), name='home_page'), 
    path('recipe/<int:pk>', RecipePageView.as_view(), name='recipe'),
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'), 

]