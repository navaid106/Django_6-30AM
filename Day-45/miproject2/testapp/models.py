from django.db import models

# Note: Based on our requiremnt, we can define our own new methods also inside CustomerManager class.
class CustomManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().order_by('eno')
        return qs
    


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=80)

    objects = CustomManager()


class ProxyEmployee(Employee):
    class Meta:
        proxy = True



