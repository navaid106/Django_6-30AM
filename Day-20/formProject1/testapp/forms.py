from django import forms

# create form class and create field with in the class.

class StudentForm(forms.Form):
    # name, marks
    name = forms.CharField()
    marks = forms.DecimalField()
    rollno = forms.IntegerField()
    dob = forms.DateField()


