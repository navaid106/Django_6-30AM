from django.db import models


class Student(models.Model):
    # rollno, name, course, date

    rollno = models.IntegerField()
    name = models.CharField(max_length=40)
    course = models.CharField(max_length=80)
    date = models.DateField()