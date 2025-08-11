from django.db import models

class Course(models.Model):
    # name, description, price, image
    name = models.CharField(max_length=40)
    # null = False [means not required]
    # null = True [means required]
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

# settings.py
    # 1. media urls ---> logical name to access media files
    # 2. media root ---> physical path of media


    # media/products/ [images]
