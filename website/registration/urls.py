from django.urls import path
from users.views import ResetPasswordView
from . import views



urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/", views.login_user, name="login"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    
]
