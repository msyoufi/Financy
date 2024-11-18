from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("login", view=views.login_view, name="login"),
    path("logout", view=views.logout_view, name="logout"),
    path("register", view=views.register_view, name="register"),
    path("transactions", view=views.transactions_view, name="transactions"),
    path("transactions/<int:tranx_id>", view=views.transactions),
]
