# movie_play/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cinema.urls')),  # This makes '' route go to cinema's views.home
]
