from urllib.parse import urlparse
from django.urls import URLPattern, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from AccountManagement.views import logout_view
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('build_view/<int:pk>/', views.build_view, name='view')
]

urlpatterns += staticfiles_urlpatterns()