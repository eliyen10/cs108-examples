from django.urls import path
from .views import ShowAllProfilesView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="home_page"),
]



    # ShowAllProfilesView