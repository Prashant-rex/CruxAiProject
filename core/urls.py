from django.urls import path
from .import views

urlpatterns = [
    path('foodtrucks/', views.FoodTruckView.as_view())
]