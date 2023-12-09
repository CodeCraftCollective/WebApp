from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include("main.urls")),
    path('hangman_menu/', views.menu, name='hangman_menu'),
    path("hangman/<int:id>/", views.hangman, name="hangman"),
]
