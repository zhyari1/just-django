from django.contrib import admin
from .models import Category, Transaction

# models in Admin dashboard is Highly Required for backend dev
admin.site.register(Transaction)
admin.site.register(Category)