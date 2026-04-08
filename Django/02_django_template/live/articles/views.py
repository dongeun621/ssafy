from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'dongeun'
    company = 'ssafy'
    context = {
        'name': name,
        'company': company
    }
    return render(request, 'articles/index.html', context)

import random
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
    }

    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)
def detail(request, num):
    context = {
        'article_id': num
    }
    return render(request, 'articles/detail.html', context)