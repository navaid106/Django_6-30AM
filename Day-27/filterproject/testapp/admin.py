from django.contrib import admin

from testapp.models import FilterModel

class FitlerModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']


admin.site.register(FilterModel,FitlerModelAdmin)
