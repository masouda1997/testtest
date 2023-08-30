from django.urls import path
from .views import *

app_name = "aut"

# urlpatterns = [
#     path("", home, name="home"),
#     path("login/", login_user, name="login"),
#     path("logout/", logout_user, name="logout"),
#     path("registration/", registration_user, name="regisregistration"),
# ]

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "registration/", registration_user, name="registration"
    ),  # Updated name parameter
]
