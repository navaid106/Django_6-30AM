from django.shortcuts import render
import requests

def home_view(request):
    # define news category
    category = [
        'technology',
        'sports',
        'health',
        'bussiness',
        'entertainment',
        'general',
    ]

    dict = {'category':category}

    return render(request,'testapp/home.html', context=dict)


def news_view(request,category):
    # API_KEY = '7bfb4e480a4f4b39930853d249c67a8d'

    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=7bfb4e480a4f4b39930853d249c67a8d"

    response = requests.get(url)
    data = response.json()

    # Extract ariticles list from API response

    articles = data.get('articles',[]) if data.get('status') == 'ok' else []

    dict = {
        'articles':articles,
        'category':category

    }

    return render(request, 'testapp/news_list.html', context=dict)





