from django.urls import path
from fullandfit import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('restaurants', views.restaurants_page, name="restaurants"),
    path('menu', views.menu_page, name="menu"),
    path('order', views.order_page, name="order"),
]
