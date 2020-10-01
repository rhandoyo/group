from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse


from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
 
]
