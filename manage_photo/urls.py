from django.contrib import admin
from django.urls import path
from .views import signupfunc,loginfunc,menufunc,Createfunc

urlpatterns = [
    path('signup/',signupfunc,name='signup'),
    path('login/',loginfunc,name='login'),
    path('menu/',menufunc,name='menu'),
    path('create/',Createfunc.as_view(),name='create'),
]