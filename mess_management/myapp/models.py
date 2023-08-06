from django.db import models


class MessUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.username


class StudentLogin(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)


class Student(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    admission_no = models.IntegerField( null=True, blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    year_of_studey=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    student_phone=models.CharField(max_length=20,null=True,blank=True)
    parent_phone=models.CharField(max_length=20,null=True,blank=True)
    last_sem_cgpa=models.CharField(max_length=20,null=True,blank=True)
    sc_st=models.BooleanField(default=False)
    bpl=models.CharField(max_length=100,null=True,blank=True)
    handicaped=models.CharField(max_length=100,null=True,blank=True)
    adhar_nu=models.BigIntegerField(null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    income=models.IntegerField(null=True,blank=True)
    caste=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    distance_from_home=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=16)
    image1=models.FileField(null=True,blank=True)
    income_certificate=models.FileField(null=True,blank=True)
    caste_certificate=models.FileField(null=True,blank=True)
    physicaly_handicaped=models.FileField(null=True,blank=True)
    ration_card=models.FileField(null=True,blank=True)
    mark_list=models.FileField(null=True,blank=True)
    uid=models.FileField(null=True,blank=True)

    def __str__(self) -> str:
        return self.username


class StudentMessDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    breakfast = models.BooleanField(default=False, null=True, blank=True)
    lunch = models.BooleanField(default=False, null=True, blank=True)
    dinner = models.BooleanField(default=False, null=True, blank=True)
    evening = models.BooleanField(default=False, null=True, blank=True)
    booking_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    payment = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.student.name + "_" + str(self.booking_date)


Choices = [
    ("sunday", "sunday"),("monday", "monday"),("tuesday", "tuesday"),(
        "wednesday", "wednesday"
    ),("thursday", "thursday"),("friday", "friday"),("saterday", "saterday")
]


class MessMenu(models.Model):
    mess_day = models.CharField(max_length=100, choices=Choices)
    breakfast = models.CharField(max_length=254, null=True, blank=True)
    lunch = models.CharField(max_length=254, null=True, blank=True)
    evening=models.CharField(max_length=254, null=True, blank=True)
    dinner = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self) -> str:
        return self.mess_day


class BillModel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    billed_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.student.name


class Cost(models.Model):
    breakfast_cost = models.IntegerField(default=10)
    dinner_cost = models.IntegerField(default=10)
    lunch_cost = models.IntegerField(default=10)
    evening_cost=models.IntegerField(default=5)

    def __str__(self) -> str:
        return "Cost"


