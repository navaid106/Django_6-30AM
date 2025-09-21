from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')

@login_required
def python_page_view(request):
    return render(request,'testapp/pythonexams.html')

@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexams.html')



from django.contrib.auth import logout
def logout_view(request):
    logout(request) 
    return render(request, 'testapp/logout.html')



from django.http import HttpResponseRedirect
from testapp.forms import SignUpForm
def singup_view(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()

        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})