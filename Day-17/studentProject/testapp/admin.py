from django.contrib import admin
from testapp.models import Student


class StudentAdmin(admin.ModelAdmin):
 # Show these columns in admin list view
    list_display = ['rollno', 'name', 'marks', 'email']

 # Add search box (by name or roll number)
    search_fields = ['name', 'rollno']

 # Add filter sidebar (by marks)
    list_filter = ['marks']

 # Sort by roll number by default
    ordering = ['rollno']

# Register the model and admin class
admin.site.register(Student,StudentAdmin)