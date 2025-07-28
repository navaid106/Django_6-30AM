from django.db import models

class Student(models.Model):
    # rollno and name
    rollno = models.IntegerField()
    name = models.CharField(max_length=40)
