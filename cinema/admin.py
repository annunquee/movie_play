# cinema/admin.py

from django.contrib import admin
from .models import Movie, Seat  # (if you have these)

admin.site.register(Movie)
admin.site.register(Seat)
