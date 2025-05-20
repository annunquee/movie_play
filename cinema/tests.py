from django.test import TestCase
from cinema.models import Movie, Seat, DailyMovie, CinemaBooking
from users.models import User
from datetime import datetime, timedelta

class CinemaModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.movie = Movie.objects.create(title='Test Movie', description='A test movie description.')
        cls.seat = Seat.objects.create(row='A', seat_number='1')
        cls.daily_movie = DailyMovie.objects.create(
            movie=cls.movie,
            show_time=datetime.now() + timedelta(days=1),
            description='Evening show'
        )

    def test_create_booking(self):
        booking = CinemaBooking.objects.create(
            movie_show=self.daily_movie,
            seat=self.seat,
            user=self.user
        )
        self.assertEqual(CinemaBooking.objects.count(), 1)
        self.assertFalse(self.seat.is_available)

    def test_double_booking_raises_error(self):
        CinemaBooking.objects.create(movie_show=self.daily_movie, seat=self.seat, user=self.user)
        with self.assertRaises(ValueError):
            CinemaBooking.objects.create(movie_show=self.daily_movie, seat=self.seat, user=self.user)
