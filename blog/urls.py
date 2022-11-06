from django.conf.urls.static import static
from django.urls import path

from my_site import settings
from .views import *


urlpatterns = [
    path('', index, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)