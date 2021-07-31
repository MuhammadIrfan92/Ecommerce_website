from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from .views import Login,Signup

urlpatterns =[
    path('',views.main,name='main'),
    path('store',views.main,name='main'),
    path('signup',Signup.as_view()),
    path('login',Login.as_view()),

    path('store/<str:header>',views.content,name='content'),
    path('checkout/<str:header>',views.checkout,name='checkout'),


]