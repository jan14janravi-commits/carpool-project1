from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ride/new/', views.RideCreateView.as_view(), name='ride_create'),
    path('ride/<int:pk>/', views.ride_detail, name='ride_detail'),
    path('ride/<int:pk>/book/', views.book_ride, name='book_ride'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-rides/', views.my_rides, name='my_rides'),
    path('register/', views.register, name='register'),
    path('users/signup/', views.register, name='register_alt'),  # Alternative URL pattern
]