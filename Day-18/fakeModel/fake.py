import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeModel.settings')

import django
django.setup()

from testapp.models import Student

from faker import Faker
fake = Faker()

def generate(n):
    # rollno, name, course, date
    course = ['BCA', 'MCA','B.Tech','M.Tech','BBA','BA','MBA','MA']
    for i in range(n):
        frollno = fake.random_int(min=100, max=999)
        fname = fake.name()
        fcourse = fake.random_element(elements=course)
        fdate = fake.date()

        Student.objects.get_or_create(rollno=frollno,name=fname,course=fcourse,date=fdate)

    


n = int(input('Enter no. of records: ')) #5
generate(n)

print('Record inserted successfully!')