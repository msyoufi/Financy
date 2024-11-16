from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ("FOOD", "Food & Dining"),
        ("TRANS", "Transportation"),
        ("SHOP", "Shopping"),
        ("BILLS", "Bills & Utilities"),
        ("OTHER", "Other"),
    ]

    TYPE_CHOICES = [("EXP", "Expense"), ("INC", "Income")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.description}"
