from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Transaction, User
from django.http import HttpResponseRedirect


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            error_message = "Passwords do not match"
            return render(request, "register.html", {"error_message": error_message})

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            error_message = "Username already taken"
            return render(request, "register.html", {"error_message": error_message})

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    user = request.user

    if user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            error_message = "Invalid Username and/or Password"
            return render(request, "login.html", {"error_message": error_message})

    user = request.user

    if user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html")


@login_required
def index(request):
    if request.method == "POST":
        pass

    return render(request, "index.html")
