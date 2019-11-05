import os
import pathlib
from FullandFitApp.nutrition_optimization import *
from FullandFitApp.csv_parse import *


from django.shortcuts import render, redirect
from FullandFitSite.settings import STATIC_ROOT

IMG_DIR = os.path.join(STATIC_ROOT, "img")

def index(request):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def restaurants_page(request):
    thumbnail_path = os.path.join(IMG_DIR, "thumbnails")
    thumbnails = os.listdir(thumbnail_path)

    ctx = {"thumbnails": thumbnails}

    return render(request, "restaurants.html", context=ctx)


def menu_page(request):



    # make database selection
    menu = read_menu(os.path.join(STATIC_ROOT, "Menu_CSV/Carl's_Jr_Menu.csv"))

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:
        item_list = request.POST.getlist('items')
        params = request.POST.dict()
        print(params)

        for id in item_list:
            id = int(id)
            items.append(menu[id])

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
            items = get_target(items, nutrient, value)
        elif algorithm == "max":
            items = get_max(items, nutrient, price)

        if price > 0:
            items = remove_items_conditionally(items, "price", lambda x, y: x <= y, limit=price)
    else:
        items = menu

    ctx = {"items": items}

    return render(request, "menu.html", context=ctx)


def order_page(request):
    return render(request, "order.html")
