from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include("main.urls")),

    path("hangman/", views.hangman, name="hangman"),
]
