from django.urls import path, re_path
from FullandFitApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('restaurants', views.restaurants_page, name="restaurants"),
    path('menu/<menu_id>/<restaurant_name>/', views.menu, name="menu"),
    path('order/<int:combo_id>/', views.order_page, name="order"),
]
