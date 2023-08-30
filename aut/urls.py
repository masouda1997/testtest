from django.urls import path
from . import views

urlpatterns = [
    path("basiclogin/", views.login_view, name="basiclogin"),
    path("basiclogout/", views.logout_view, name="basiclogout"),
]
