import os
from FullandFitApp.nutrition_optimization import *
from FullandFitApp.parsing.csv_parse import *
from FullandFitApp.restaurant.restaurant_objects import *


from django.shortcuts import render, redirect
from FullandFitSite.settings import STATIC_ROOT

IMG_DIR = os.path.join(STATIC_ROOT, "img")

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
    current_restaurant.menu = get_menu_from_csv(os.path.join(STATIC_ROOT, "Menu_CSV/{}.csv".format(menu_csvfile)))

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:
        item_ids = request.POST.getlist('items')
        params = request.POST.dict()

        for item_id in item_ids:
            item_id = int(item_id)
            items.append(current_restaurant.menu[item_id].to_dict())

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

        if algorithm == "target":
            items = get_target(items, nutrient, value, price)
        elif algorithm == "max":
            items = get_max(items, nutrient, price)
    else:
        items = current_restaurant.get_menu_item_dictionary_array()

    ctx = {"restaurant_name": current_restaurant.name, "menu": items}

    return render(request, "menu.html", context=ctx)

def order_page(request):
    return render(request, "order.html")
