import os
from FullandFitApp import nutrition_optimization
from FullandFitApp.parsing.csv_parse import *
from FullandFitApp.restaurant.restaurant_objects import *

from django.shortcuts import render, redirect
from django.contrib import messages

from FullandFitSite.settings import STATIC_ROOT


IMG_DIR = os.path.join(STATIC_ROOT, "img")

current_restaurant = Restaurant()
current_combos = []


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
    global current_combos

    # todo: convert to draw from database
    menu_csvfile = menu_id.split('.')[0]

    # todo: refactor the current restaurant building to another function
    current_restaurant.name = restaurant_name.split('.')[0]
    menu_items = get_menu_from_csv(os.path.join(STATIC_ROOT, "Menu_CSV/{}.csv".format(menu_csvfile)))
    current_restaurant.menu = Menu(menu_items)

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:

        item_ids = request.POST.getlist('items')
        params = request.POST.dict()

        for item_id in item_ids:
            if item_id is "":
                continue
            item_id = int(item_id)
            items.append(current_restaurant.menu.get_item_by_id(item_id))

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

        # if price is 0, don't consider it
        if price == 0:
            price += 99999

        if algorithm == "less_than":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = current_restaurant.menu.get_combos_and_filter(
                    nutrient,
                    value,
                    lambda x, y: x <= y,
                    price
                )
                items = compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")
        elif algorithm == "exactly":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = current_restaurant.menu.get_combos_and_filter(
                    nutrient,
                    value,
                    lambda x, y: 0.9 * y <= x <= 1.1 * y,
                    price
                )
                items = compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")
        elif algorithm == "greater_than":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = current_restaurant.menu.get_combos_and_filter(
                    nutrient,
                    value,
                    lambda x, y: x >= y,
                    price
                )
                items = compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")
    else:
        items = current_restaurant.menu.to_dictionary_array()

    ctx = {"restaurant_name": current_restaurant.name, "menu": items}

    return render(request, "menu.html", context=ctx)


def order_page(request):
    return render(request, "order.html")
