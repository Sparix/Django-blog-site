from django import template
from blog.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if sort is None:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def show_header():
    menu = [{'title': "Home", 'url_name': 'home'},
            {'title': "Posts", 'url_name': 'post'},
            {'title': "MyPosts", 'url_name': 'userpost'}]
    return menu
