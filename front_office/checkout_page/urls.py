from django.urls import path
from . import views

app_name = "checkout_page"

urlpatterns = [
    path("", views.checkout, name="checkout"),
]
