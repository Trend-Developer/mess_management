from django.urls import path, include
from .views import user_login

urlpatterns = [
    path("login/",user_login)
]
