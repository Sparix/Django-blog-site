from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# from .utils import *
from .forms import *
from .models import *

count_cat = Categories.objects.annotate(Count('car'))
menu_bar = {'fa-home': 'home', 'fa-twitter': 'homes'}
menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Posts', 'url_name': 'post'},
        {'title': 'MyPosts', 'url_name': 'userpost'}]


class CarHome(ListView):
    paginate_by = 4
    model = Car
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        context['cat_selected'] = 0
        context['count_cat'] = count_cat
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context

    def get_queryset(self):
        return Car.objects.filter(is_published=True)


'''def index(request):
    return render(request, 'index.html', context=context)'''


class ShowPost(DetailView):
    model = Car
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context


'''def show_post(request, post_slug):
    test = Car.objects.filter(slug=post_slug)

    context = {'menu_bar': menu_bar,
               'posts': posts,
               'categor': categor,
               'count_cat': count_cat,
               'post': test
               }
    return render(request, 'post.html', context=context)'''


class ShowCategory(ListView):
    paginate_by = 4
    model = Car
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        context['cat_selected'] = context['posts'][0].cat_id
        context['count_cat'] = count_cat
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context


'''def show_category(request, cat_slug):
    cat = Car.objects.filter(slug=cat_slug)
    if len(posts) == 0:
        raise Http404()

    context = {
        'menu_bar': menu_bar,
        'posts': posts,
        'cat': cat,
        'categor': categor,
        'count_cat': count_cat,
        'cat_selected': cat_slug,
    }
    return render(request, 'index.html', context=context)
'''

'''def login(request):
    return render(request, 'login.html', context=context)'''


class RegisterUser(CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context


'''def register(request):
    return render(request, 'register.html', context=context)
'''


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


'''def account(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {'menu_bar': menu_bar,
               'posts': posts,
               'categor': categor,
               'count_cat': count_cat,
               'cat_selected': 0,
               'form': form
               }
    return render(request, 'account.html', context=context)'''


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context

    def get_success_url(self):
        return reverse_lazy('account')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShowPostUser(ListView):
    paginate_by = 4
    model = Car
    template_name = 'user_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        cars_user = Car.objects.filter(author=self.request.user, is_published=True)
        return cars_user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_bar'] = menu_bar
        context['cat_selected'] = 0
        context['count_cat'] = count_cat
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context
