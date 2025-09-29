from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Class Based Views

class HelloWorld(View):
    def get(self, request):
        return HttpResponse('<h1 style="color:red">Hello.. This response is from class based views </h1>')
        
class TemplateCBV(TemplateView):
    template_name = 'testapp/results.html'

# Send content Dictionary using CBVs

class TemplateCBV2(TemplateCBV):
    template_name = 'testapp/results2.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Nobita'
        context['rollno'] = 101
        context['course'] = 'Django'

        return context
