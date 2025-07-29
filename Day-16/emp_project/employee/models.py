from django.db import models

# Create your models here.

class Employee(models.Model):
    # name, age, department, email
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
