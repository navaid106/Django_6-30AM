from django.shortcuts import render

# Home Page
def news_info(request):
    return render(request, 'testapp/index.html')

def movie_view(request):
    heading = "Movies information Heading..."
    sub1 = "xyz is a nice moive"
    sub2 = "lucy is a nice"
    sub3 = "upcoming movie..."

    type='movie'

# dictonary ===> {key:value}
    dict = {'heading':heading,'sub1':sub1,'sub2':sub2,'sub3':sub3,'type':type}

    return render(request, 'testapp/news.html',context=dict)

def sport_view(request):
    heading = "Sports information Heading..."
    sub1 = "xyz is a nice sport"
    sub2 = "abc is a nice"
    sub3 = "upcoming sports..."

    type='sport'

# dictonary ===> {key:value}
    dict = {'heading':heading,'sub1':sub1,'sub2':sub2,'sub3':sub3,'type':type}

    return render(request, 'testapp/news.html',context=dict)

def politics(request):
    heading = "Politics information Heading..."
    sub1 = "xyz is a nice "
    sub2 = "lucy is a nice"
    sub3 = "upcoming politics..."

    type='politic'

# dictonary ===> {key:value}
    dict = {'heading':heading,'sub1':sub1,'sub2':sub2,'sub3':sub3,'type':type}

    return render(request, 'testapp/news.html',context=dict)
