from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Ride(models.Model):
    DRIVER_TYPE_CHOICES = [
        ('driver', 'Driver'),
        ('co_driver', 'Co-Driver'),
    ]
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_offered')
    title = models.CharField(max_length=120)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    seats_total = models.PositiveIntegerField(default=4)
    seats_available = models.PositiveIntegerField()
    price_per_seat = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date', '-time')

    def save(self, *args, **kwargs):
        if self.seats_available is None:
            self.seats_available = self.seats_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} — {self.origin} → {self.destination} on {self.date}"

    def get_absolute_url(self):
        return reverse('ride_detail', args=[str(self.id)])


class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    seats_booked = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ride', 'user')  # a user can book a ride once

    def __str__(self):
        return f"{self.user.username} booked {self.seats_booked} seat(s) on {self.ride}"