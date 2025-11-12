from django.urls import path
from  import views

urlpatterns = [
    path('suggest/', views.suggest_ride, name='suggest_ride'),
]
