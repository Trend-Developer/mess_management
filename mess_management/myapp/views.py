from django.shortcuts import render
from .models import MessUser, Student, StudentMessDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentMessDetails_Serializer

"""
payload username , password , type_of_user
"""


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
        return Response({"data": data})


"""
payload -- username , name ,password , cm_password , type_of_user
"""


@api_view(["POST"])
def register_user(request):
    data = request.data
    if (
        MessUser.objects.filter(username=data["username"]).exists()
        or Student.objects.filter(username=data["username"]).exclude()
    ):
        return Response({"message": "username already exist", "success": False})

    if data["password"] is not data["cm_password"]:
        return Response({"message": "password miss match", "success": False})
    type_of_user = data["type_of_user"]
    current_model = None
    if type_of_user == "student":
        current_model = Student
    else:
        current_model = MessUser

    obj = current_model.objects.create(
        name=data["name"], username=data["username"], password=data["password"]
    )
    obj.save()
    user_obj = current_model.objects.get(username=data["username"])
    user_data = {
        "id": user_obj.id,
        "name": user_obj.name,
        "username": user_obj.username,
    }
    return Response({"data": user_data, "success": True})


"""
payload - booking_date,username ,evening ,breakfast , lunch ,dinner
"""


@api_view(["POST"])
def book_mess(request):
    data = request.data
    booking_date = data["booking_date"]
    username = data["username"]

    student_obj = Student.objects.get(username=username)
    if StudentMessDetails.objects.filter(
        booking_date=booking_date, Student=student_obj
    ).exists():
        return Response({"message": "already booked", "success": False})

    else:
        details_obj = StudentMessDetails.objects.create(
            Student=student_obj,
            breakfast=data["breakfast"],
            lunch=data["lunch"],
            dinner=data["dinner"],
            evening=data["evening"],
            booking_date=booking_date,
        )
        details_obj.save()
        return Response({"message": "booked successfully", "sucess": True})


@api_view(["GET"])
def view_booked(request, username):
    data = StudentMessDetails.objects.filter(student__username=username)
    seria = StudentMessDetails_Serializer(data, many=True)
    return Response(seria.data)
