# movies/views.py
from django.shortcuts import render
from django.conf import settings
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = settings.TMDB_API_KEY

def movie_list(request):
    movie = Movie()
    popular = movie.popular()
    return render(request, 'movies/movie_list.html', {'movies': popular})
