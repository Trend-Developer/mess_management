from django.shortcuts import render
from .models import MessUser, Student
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def user_login(request):
    username = request.data["username"]
    password = request.data["password"]
    data_model = None
    if request.data["type_of_user"] == "mess_user":
        data_model = MessUser
    else:
        data_model = Student

    if not data_model.objects.filter(username=username).exists():
        return Response({"message": "user not found"})

    user_obj = data_model.objects.get(username=username)
    if user_obj.password != password:
        return Response({"message": "password in incorrect"})
    
    else:
        data = {
            "id": user_obj.id,
            "name": user_obj.name,
            "username": user_obj.username,
        }
        return Response({"data":data})
    
