from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", user_login),
    path("register_user/", register_user),
    path("book_mess/", book_mess),
    path("view_booked/", view_booked),
    path("get_messmenu/", get_messmenu),
    path("billing/", billing),
]
