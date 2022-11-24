'''posts = Car.objects.all()
categor = Categories.objects.all()
count_cat = Categories.objects.annotate(Count('car'))

context = {'menu_bar': menu_bar,
           'posts': posts,
           'categor': categor,
           'count_cat': count_cat,
           'cat_selected': 0,
           }
from .models import *

menu_bar = {'fa-home': 'home', 'fa-twitter': 'homes'}


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Categories.objects.all()
        context['menu_bar'] = menu_bar
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
'''