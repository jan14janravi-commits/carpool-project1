from django import forms
from .models import Ride, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RideForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Ride
        fields = ['title','origin','destination','date','time','seats_total','seats_available','price_per_seat','description']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats_booked']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")