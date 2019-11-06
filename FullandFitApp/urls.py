from django.urls import path, re_path
from FullandFitApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('restaurants', views.restaurants_page, name="restaurants"),
    path('menu/<menu_id>/', views.menu, name="menu"),
    path('order', views.order_page, name="order"),
]
