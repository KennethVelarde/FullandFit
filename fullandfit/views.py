from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def restaurants_page(request):
    return render(request, "restaurants.html")


def menu_page(request):
    return render(request, "menu.html")


def order_page(request):
    return render(request, "order.html")
