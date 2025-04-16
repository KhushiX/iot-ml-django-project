
# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.get_prediction),
    # For fetching the latest sensor data
    path('predict/', views.get_prediction),  
      # For predicting based on sensor data
]
