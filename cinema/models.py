# cinema/models.py 
from django.db import models
from users.models import User  # Custom user model

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # poster = models.ImageField(upload_to="posters/", null=True, blank=True)

    def __str__(self):
        return self.title


class Seat(models.Model):
    row = models.CharField(max_length=5)  # e.g., A, B, C, D
    seat_number = models.CharField(max_length=10)  # e.g., 1, 2, 3
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('row', 'seat_number')  # Prevent duplicates

    def __str__(self):
        return f"Row {self.row} Seat {self.seat_number}"


class DailyMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="daily_showings")
    show_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.movie.title} at {self.show_time.strftime('%I:%M %p')}"


class CinemaBooking(models.Model):
    movie_show = models.ForeignKey(DailyMovie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seat} for {self.movie_show}"

    def save(self, *args, **kwargs):
        # Only book if seat is available
        if self.seat.is_available:
            self.seat.is_available = False
            self.seat.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError(f"Seat {self.seat} is already booked.")
