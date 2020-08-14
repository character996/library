from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('login_check', views.login_check, name='login_check'),
    path('borrow_history/', views.borrow_history, name='borrow_history'),
    path('borrow_info/', views.borrow_info, name='borrow_info'),
    path('book_search/', views.book_search, name='book_search'),
    path('balance_change/', views.balance_change, name='balance_change'),
    path('user/', views.user, name='user'),
    path('return_book/', views.return_book, name='return_book'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
]
