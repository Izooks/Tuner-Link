from django.urls import path 

from . import views 

app_name = 'AccountManagement'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]