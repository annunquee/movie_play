from django.db import models
from users.models import User

class DailyMovie(models.Model):
    title = models.CharField(max_length=200)
    show_time = models.DateTimeField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.show_time.strftime('%I:%M %p')}"

class CinemaBooking(models.Model):
    movie = models.ForeignKey(DailyMovie, on_delete=models.CASCADE, related_name="bookings")
    seat_number = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)  # Later you can link this to Django's User model
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.movie.title} - Seat {self.seat_number}"
