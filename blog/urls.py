from django.conf.urls.static import static
from django.urls import path

from my_site import settings
from .views import *


urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='category'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('account_addpage', AddPage.as_view(), name='account'),
    path('users', ShowPostUser.as_view(), name='users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)