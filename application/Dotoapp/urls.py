from django.urls import path
from . import views


urlpatterns = [
    path("", views.view, name="Home"),
    path("transactions/", views.transactions, name="transactions-list"),   #  There is no need for / at first always at the end 
]
