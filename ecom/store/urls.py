from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from .views import Checkout, Login,Signup,Cart

urlpatterns =[
    path('',views.main,name='main'),
    path('store',views.main,name='main'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),

    path('store/<str:header>',views.content,name='content'),
    path('checkout',Checkout.as_view(),name='checkout'),


]