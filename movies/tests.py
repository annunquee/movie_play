from django.test import TestCase
from tmdbv3api import Movie

class MovieViewTests(TestCase):
    def test_tmdb_api_returns_results(self):
        movie = Movie()
        results = movie.popular()
        self.assertGreater(len(results), 0, "Expected popular movies list to be non-empty.")
