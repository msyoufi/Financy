from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("login", view=views.login_view, name="login"),
    path("logout", view=views.logout_view, name="logout"),
    path("register", view=views.register_view, name="register"),
]
