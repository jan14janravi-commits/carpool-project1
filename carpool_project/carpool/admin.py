from django.contrib import admin
from .models import Ride, Booking

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('title','driver','origin','destination','date','time','seats_available')
    search_fields = ('title','origin','destination','driver__username')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('ride','user','seats_booked','booked_at')