from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path('menu/', views.menu, name='menu'),
    path('view/<int:id>/', views.view, name='view'),
    path("", views.home, name="home"),
    path("lists/", views.lists, name="lists"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path("admin_approval/", views.admin_approval, name="admin_approval"),
]
