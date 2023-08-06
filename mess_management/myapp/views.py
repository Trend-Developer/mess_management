from django.shortcuts import render
from .models import MessUser, Student, StudentMessDetails, MessMenu, BillModel,StudentLogin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentMessDetails_Serializer, StudentRegistrationSerializer
from datetime import datetime, timedelta
from datetime import date

"""
payload username , password , type_of_user
"""


@api_view(["POST"])
def user_login(request):
    username = request.data["username"]
    password = request.data["password"]
    data_model = StudentLogin
    # if request.data["type_of_user"] == "mess_user":
    #     data_model = MessUser
    # else:
    #     data_model = Student

    if not data_model.objects.filter(username=username).exists():
        return Response({"message": "user not found"})

    user_obj = data_model.objects.get(username=username)
    if user_obj.password != password:
        return Response({"message": "password in incorrect"})

    else:
        data = {
            "id": user_obj.id,
            "username": user_obj.username,
        }
        return Response({"data": data})


"""
payload -- username , name ,password , cm_password , type_of_user
"""


@api_view(["POST"])
def register_messuser(request):
    data = request.data
    if MessUser.objects.filter(username=data["username"]).exists():
        return Response({"message": "username already exist", "success": False})

    if data["password"] is not data["cm_password"]:
        return Response({"message": "password miss match", "success": False})
    type_of_user = data["type_of_user"]
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
    booking_date = str(data["selectedDate"]).split("T")[0]
    username = data["username"]

    student_obj = Student.objects.get(username=username)
    if StudentMessDetails.objects.filter(
        booking_date=booking_date, student=student_obj
    ).exists():
        return Response({"message": "already booked", "success": False})

    else:
        details_obj = StudentMessDetails.objects.create(
            student=student_obj,
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


@api_view(["GET"])
def get_messmenu(request):
    menu_obj = MessMenu.objects.all()
    days = [obj.mess_day for obj in menu_obj]
    breakfast = [obj.breakfast for obj in menu_obj]
    lunch = [obj.lunch for obj in menu_obj]
    evening = [obj.evening for obj in menu_obj]
    dinner = [obj.dinner for obj in menu_obj]
    mess_day = {
        "days": days,
        "breakfast": breakfast,
        "lunch": lunch,
        "evening": evening,
        "dinner": dinner,
    }
    return Response({"data": mess_day})


@api_view(["POST"])
def billing(request):
    month = int(request.data["month"])
    year = int(request.data["year"])
    username = request.data["username"]
    start_date = datetime(year, month, 1)  # first of month
    end_date = datetime(year, month + 1,1)  # last of month
    foo_date = StudentMessDetails.objects.filter(
        student__username=username, booking_date__range=(start_date, end_date)
    )
    count = foo_date.count()
    if count<=0:
        return Response({"success": True, "billed_amount": 0})
    total_bill = 0
    for bill in foo_date[0:count-1]:
        if bill.breakfast:
            total_bill = total_bill + 10
        if bill.lunch:
            total_bill = total_bill + 10
        if bill.dinner:
            total_bill = total_bill + 10
        if bill.evening:
            total_bill = total_bill + 10

    return Response({"success": True, "billed_amount": total_bill})


@api_view(["POST"])
def student_registrations(request):
    seria = StudentRegistrationSerializer(data=request.data)
    if seria.is_valid():
        seria.save()
        return Response({"message": "saved successfully", "data": seria.data})
    return Response({"message": "failed to save", "data": seria.errors})
