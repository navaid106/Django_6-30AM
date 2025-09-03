from django.db import models

class FilterModel(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    dept = models.CharField(max_length=40)
    date = models.DateField()
