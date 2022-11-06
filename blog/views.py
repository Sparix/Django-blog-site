from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.db.models import Count

from .models import *


def index(request):
    posts = Car.objects.all()
    categor = Categories.objects.all()
    count_cat = Categories.objects.annotate(Count('car'))
    header = ['Home', 'My post', 'Posts']
    menu_bar = {'fa-home': 'Home', 'fa-twitter': 'homes'}
    return render(request, 'index.html',
                  {'header': header, 'menu_bar': menu_bar, 'posts': posts, 'categor': categor, 'count_cat': count_cat})
