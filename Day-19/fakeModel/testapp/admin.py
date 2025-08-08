from django.contrib import admin
from testapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','course','date']

    search_fields = ['rollno','course']

    list_filter = ['rollno']

admin.site.register(Student,StudentAdmin)



