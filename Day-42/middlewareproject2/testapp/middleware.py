from django.http import HttpResponse

class AppMaintenanceMiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response
        

    def __call__(self, request):
        return HttpResponse('<h1>Currently.. Application is under maintenance.. please try after 3-days...</h1>')