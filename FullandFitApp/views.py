import os
import pathlib
from FullandFitApp.nutrition_optimization import *
from FullandFitApp.csv_parse import *


from django.shortcuts import render, redirect
from FullandFitSite.settings import STATIC_ROOT

IMG_DIR = os.path.join(STATIC_ROOT, "img")


class Restaurant:
    def __init__(self):
        self.name = None
        self.logopath = None
        self.menu = None
        self.csvfile = None


current_restaurant = Restaurant()


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def restaurants_page(request):
    thumbnail_path = os.path.join(IMG_DIR, "thumbnails")
    thumbnails = os.listdir(thumbnail_path)

    ctx = {"thumbnails": thumbnails}

    return render(request, "restaurants.html", context=ctx)


def menu(request, menu_id, restaurant_name):
    global current_restaurant

    # todo: convert to draw from database
    menu_csvfile = menu_id.split('.')[0]

    # todo: refactor the current restaurant building to another function
    current_restaurant.name = restaurant_name.split('.')[0]
    current_restaurant.menu = read_menu(os.path.join(STATIC_ROOT, "Menu_CSV/{}.csv".format(menu_csvfile)))

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:
        item_ids = request.POST.getlist('items')
        params = request.POST.dict()

        for item_id in item_ids:
            item_id = int(item_id)
            items.append(current_restaurant.menu[item_id])

        nutrient = ""
        value = 0
        price = 0
        algorithm = params["algorithm_selection"]

        if params["price"] != '':
            price = float(params["price"])

        if params["nutrient_selection"] != '':
            nutrient = params["nutrient_selection"]

        if nutrient == "carbs":
            value = int(params["carbs"])
        elif nutrient == "protein":
            value = int(params["protein"])
        elif nutrient == "fat":
            value = int(params["fat"])
        elif nutrient == "calories":
            value = int(params["calories"])

        if algorithm == "target":
            items = get_target(items, nutrient, value, price)
        elif algorithm == "max":
            items = get_max(items, nutrient, price)

        if price > 0:
            items = remove_items_conditionally(items, "price", lambda x, y: x <= y, critical_value=price)
    else:
        items = current_restaurant.menu

    ctx = {"restaurant_name": current_restaurant.name, "menu": items}

    return render(request, "menu.html", context=ctx)

#
# def combos_page(request):



def order_page(request):
    return render(request, "order.html")
