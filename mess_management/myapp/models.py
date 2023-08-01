from django.db import models



class MessUser(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.username


class Student(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=16)
    def __str__(self) -> str:
        return self.username

