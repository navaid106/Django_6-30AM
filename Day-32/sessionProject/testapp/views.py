from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print(request.COOKIES)
    count = request.session.get('count',0)
    count+=1
    request.session['count']=count

    request.session.set_expiry(1)

    return render(request,'testapp/pageCount.html',{'count':count})
