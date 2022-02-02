from urllib.parse import urlparse
from django.urls import URLPattern, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home')
]

urlpatterns += staticfiles_urlpatterns()