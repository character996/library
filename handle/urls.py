from django.urls import path
from . import views

app_name = 'handle'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search_book/', views.search_book, name='search_book'),
    path('recharge/', views.recharge, name='recharge'),
]
