from django.contrib import admin
from .models import Transaction, User

admin.site.register(User)
admin.site.register(Transaction)
