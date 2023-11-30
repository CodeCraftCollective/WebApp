from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path('menu/', views.menu, name='menu'),
    path('view/<int:id>/', views.view, name='view'),
    path("", views.home, name="home"),
    path("lists/", views.lists, name="lists")
]
