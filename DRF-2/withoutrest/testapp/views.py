from django.shortcuts import render

from django.http import HttpResponse

import json
def emp_data_view(request):

    emp_data = {
        'eno':101,
        'ename':'Nobita',
        'esal':12000,
        'eaddr':'Mumbai'
    }

    resp = f''' <h1>
    Employee Number: {emp_data['eno']} <br>
    Employee Name: {emp_data['ename']} <br>
    Employee Salary: {emp_data['esal']}<br>
    Employee Address: {emp_data['eaddr']}</h1>
    '''

    return HttpResponse(resp)


def emp_data_json_view(request):
    emp_data = {
        'eno':102,
        'ename':'Doreamon',
        'esal':15000,
        'eaddr':'Jaipur'
    }

    # Dict ===> Json <<dumps()>>

    json_data = json.dumps(emp_data)

    return HttpResponse(json_data)



# sending direct jsonResponse

from django.http import JsonResponse
def emp_data_json_view2(request):
    emp_data = {
        'eno':103,
        'ename':'Jiyan',
        'esal':18000,
        'eaddr':'Delhi'
    }

    return JsonResponse(emp_data)



from django.views.generic import View 

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
            'eno':104,
            'ename':'Ramesh',
            'esal':34000,
            'eaddr':'Hyderabad'
        }

        return JsonResponse(emp_data)
    

from testapp.mixins import HttpResponseMixin

class JsonCBV2(View,HttpResponseMixin):
    def get(self,request,*args, **kwargs):
        dict1  = {'msg':'This is GET method'}
        # dictionary ===> json 
        json_data = json.dumps(dict1)

        return self.render_to_response(json_data)


    def post(self,request,*args, **kwargs):
        dict2 = {'msg':'This is POST method'} 
        # dictionary ===> json 
        json_data = json.dumps(dict2)

        return self.render_to_response(json_data)

    def put(self,request,*args, **kwargs):
        dict3 = {'msg':'This is PUT method'} 
        # dictionary ===> json 
        json_data = json.dumps(dict3)

        return self.render_to_response(json_data)


    def delete(self,request,*args, **kwargs):
        dict4 = {'msg':'This is DELETEE method'}
        # dictionary ===> json 
        json_data = json.dumps(dict4)

        return self.render_to_response(json_data)