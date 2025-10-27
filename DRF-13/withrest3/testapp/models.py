from django.db import models


class Employee(models.Model):
    # eno, ename, esal, eaddr 
    eno = models.IntegerField()
    ename = models.CharField(max_length=40)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=80)
    
