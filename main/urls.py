from urllib.parse import urlparse
from django.urls import URLPattern, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from AccountManagement.views import logout_view
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base')
    
]

urlpatterns += staticfiles_urlpatterns()