from django.shortcuts import render
from testapp.models import FilterModel

def upper_data_view(request):
    records = FilterModel.objects.all()
    return render(request,'testapp/index.html',{'records':records})
    
