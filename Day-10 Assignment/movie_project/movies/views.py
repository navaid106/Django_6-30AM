from django.shortcuts import render
from django.http import JsonResponse

# Dummy Movie data

movies = [
    {
        'id': 1,
        'title': 'Inception',
        'year': 2010,
        'poster': 'inception.jpeg',
    },
    {
        'id': 2,
        'title': 'The Dark Knight',
        'year': 2008,
        'poster': 'dark_knight.jpg',
    },
    {
        'id': 3,
        'title': 'Interstellar',
        'year': 2014,
        'poster': 'interstellar.jpeg',
    },
    {
        'id': 4,
        'title': 'Avengers: Endgame',
        'year': 2019,
        'poster': 'endgame',
    },
    {
        'id': 5,
        'title': 'The Matrix',
        'year': 1999,
        'poster': 'matrix',
    },
    {
        'id': 6,
        'title': 'Titanic',
        'year': 1997,
        'poster': 'titanic',
    },
    {
        'id': 7,
        'title': 'The Lion King',
        'year': 1994,
        'poster': 'lion_king',
    },
    {
        'id': 8,
        'title': 'Spider-Man: No Way Home',
        'year': 2021,
        'poster': 'no_way_home',
    },
]



def home_view(request):
    return render(request,'movies/home.html')

def movie_list_view(request):
    return render(request,'movies/movie_list.html',{'movies':movies})

def movie_detail_view(request,id):
    movie = None
    for m in movies:
        if m['id'] == id:
            movie = m
            break
    
    return render(request,'movies/movie_details.html',{'movie':movie})

def movie_json_view(request):
    return JsonResponse({'movies':movies})