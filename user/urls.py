from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('resister/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
