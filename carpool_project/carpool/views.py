from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Ride, Booking
from .forms import RideForm, BookingForm, RegisterForm
from django.contrib import messages
from django.db import transaction


def home(request):
    q = request.GET.get('q', '')
    rides = Ride.objects.all()
    if q:
        rides = rides.filter(origin__icontains=q) | rides.filter(destination__icontains=q) | rides.filter(title__icontains=q)
    return render(request, 'carpool/home.html', {'rides': rides, 'q': q})

class RideCreateView(CreateView):
    model = Ride
    form_class = RideForm
    template_name = 'carpool/ride_forms.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.driver = self.request.user
        # ensure seats_available defaults
        if not form.instance.seats_available:
            form.instance.seats_available = form.instance.seats_total
        return super().form_valid(form)

def ride_detail(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    booking_form = BookingForm()
    return render(request, 'carpool/ride_detail.html', {'ride': ride, 'booking_form': booking_form})

@login_required
def book_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats_requested = form.cleaned_data['seats_booked']
            if seats_requested <= 0:
                messages.error(request, "Invalid number of seats.")
                return redirect('ride_detail', pk=pk)
            # atomic operation to avoid race conditions
            with transaction.atomic():
                ride = Ride.objects.select_for_update().get(pk=ride.pk)
                if seats_requested > ride.seats_available:
                    messages.error(request, "Not enough seats available.")
                    return redirect('ride_detail', pk=pk)
                # create or update booking
                booking, created = Booking.objects.get_or_create(ride=ride, user=request.user,
                                                               defaults={'seats_booked': seats_requested})
                if not created:
                    # If already booked, update seats (ensure total seats not exceed)
                    new_total = booking.seats_booked + seats_requested
                    if new_total > ride.seats_total:
                        messages.error(request, "Cannot exceed total seats for this ride.")
                        return redirect('ride_detail', pk=pk)
                    booking.seats_booked = new_total
                    booking.save()
                ride.seats_available -= seats_requested
                ride.save()
                messages.success(request, "Booking successful!")
                return redirect('my_bookings')
    return redirect('ride_detail', pk=pk)

@login_required
def my_bookings(request):
    bookings = request.user.bookings.select_related('ride')
    return render(request, 'carpool/my_bookings.html', {'bookings': bookings})

@login_required
def my_rides(request):
    rides = request.user.rides_offered.all()
    return render(request, 'carpool/my_rides.html', {'rides': rides})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'carpool/register.html', {'form': form})

