from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Transaction, User
from django.http import HttpResponseRedirect
from .utils import clean_data, get_chart_data


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
    return render(request, "index.html")


@login_required
def charts(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("date")
    chart_data = get_chart_data(transactions) if transactions.exists() else {}

    return JsonResponse(chart_data, safe=False)


@login_required
def transactions_view(request):
    user = request.user

    if request.method == "POST":
        try:
            tranx_data = clean_data(request.POST)
            tranx = Transaction(user=user, **tranx_data)
            tranx.save()
            return redirect("transactions")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    transactions = Transaction.objects.filter(user=user).order_by("-date")

    categories = [
        {"code": category[0], "display": category[1]}
        for category in Transaction.CATEGORY_CHOICES
    ]

    return render(
        request,
        "transactions.html",
        {"transactions": transactions, "categories": categories},
    )


@login_required
def transactions(request, tranx_id):
    user = request.user

    if tranx_id is None:
        return JsonResponse({"error": "Must provide a transaction ID"}, status=400)

    try:
        tranx = Transaction.objects.get(user=user, id=tranx_id)
    except Transaction.DoesNotExist:
        return JsonResponse({"error": "Transaction not found!"}, status=404)

    if request.method == "GET":
        return JsonResponse(tranx.serialize(), status=200)

    if request.method == "POST":
        try:
            tranx_data = clean_data(request.POST)
            for key, value in tranx_data.items():
                setattr(tranx, key, value)
            tranx.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    if request.method == "DELETE":
        tranx.delete()

    return redirect("transactions")
