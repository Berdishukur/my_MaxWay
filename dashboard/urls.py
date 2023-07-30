from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('login_page/',login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),


    path('category/list/', category_list, name='category_list'),
    path('category/create/',category_create, name='category_create'),
    path('category/<int:pk>/edit/',category_edit,name='category_edit'),
    path('category/<int:pk>/delete/',category_delete,name='category_delete'),




    path('profile/',profile, name='profile'),
]