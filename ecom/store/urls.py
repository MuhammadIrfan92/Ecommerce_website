from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('',views.main,name='main'),
    path('store',views.main,name='main'),

    path('store/<str:header>',views.content,name='content'),
    path('checkout/<str:header>',views.checkout,name='checkout')

]