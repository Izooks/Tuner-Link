from django.urls import path, include
from . import views 

app_name = 'AccountManagement'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'), 
    path('profile', views.profile_view, name='profile'),
    path('modify', views.edit_view, name='edit'),
    path('update/<int:pk>/', views.update_car, name='update'),
    path('delete/<int:pk>/', views.delete_car, name='delete')
]