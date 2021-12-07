from django.urls import path
from .views import CreateRecipeView, HomePageView, RecipePageView, UpdateRecipeView, RandomRecipePageView # our view class definition 

urlpatterns = [
    path('', HomePageView.as_view(), name='all_recipes'), 
    path('all', RandomRecipePageView.as_view(), name='random'), 


    path('recipe/<int:pk>', RecipePageView.as_view(), name='recipe'),
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'), 
    path('recipe/<int:pk>/update', UpdateRecipeView.as_view(), name='update_recipe'),

]