from rest_framework import serializers
from .models import StudentMessDetails


class StudentMessDetails_Serializer(serializers.ModelSerializer):
    dinner = serializers.SerializerMethodField("get_dinner_status")
    breakfast = serializers.SerializerMethodField("get_breakfast_status")
    evening = serializers.SerializerMethodField("get_evening_status")
    lunch = serializers.SerializerMethodField("get_lunch_status")

    def get_dinner_status(request, obj):
        if obj.dinner == True:
            return "Booked"
        return "Not booked"

    def get_lunch_status(request, obj):
        if obj.lunch == True:
            return "Booked"
        return "Not booked"

    def get_breakfast_status(request, obj):
        if obj.breakfast == True:
            return "Booked"
        return "Not booked"

    def get_evening_status(request, obj):
        if obj.evening == True:
            return "Booked"
        return "Not booked"

    class Meta:
        model = StudentMessDetails
        fields = ["booking_date", "dinner", "evening", "lunch", "breakfast"]
