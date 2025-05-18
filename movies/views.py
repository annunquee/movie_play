# movies/views.py
from django.shortcuts import render
from decouple import config
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = config('TMDB_API_KEY')  # Directly from .env

def movie_list(request):
    movie = Movie()
    popular = movie.popular()
    return render(request, 'movies/movie_list.html', {'movies': popular})
