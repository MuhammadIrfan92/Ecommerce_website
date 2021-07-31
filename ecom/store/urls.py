from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from .views import Login,Signup,Main,Cart

urlpatterns =[
    path('',Main.as_view()),
    path('store',Main.as_view(),name='main'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),

    path('store/<str:header>',views.content,name='content'),
    path('checkout/<str:header>',views.checkout,name='checkout'),


]