import os
import pathlib
from fullandfit.nutrition_optimization import *


from django.shortcuts import render, redirect
from django.http import HttpResponse
from FullandFit.settings import STATIC_ROOT

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
    test_menu = dict()
    test_menu[0] = {"id": 0, "name": "burger", "price": 5.99, "calories": 700, "carbs": 60, "protein": 30, "fat": 10}
    test_menu[1] = {"id": 1, "name": "fries", "price": 2.50, "calories": 100, "carbs": 10, "protein": 0, "fat": 15}
    test_menu[2] = {"id": 2, "name": "coke", "price": 1.99, "calories": 150, "carbs": 60, "protein": 0, "fat": 0}
    test_menu[3] = {"id": 3, "name": "milkshake", "price": 2.99, "calories": 400, "carbs": 100, "protein": 20, "fat": 15}
    test_menu[4] = {"id": 4, "name": "chicken sandwich", "price": 6.99, "calories": 615, "carbs": 60, "protein": 30, "fat": 15}
    test_menu[5] = {"id": 5, "name": "salad", "price": 4.99, "calories": 100, "carbs": 0, "protein": 0, "fat": 15}

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:
        item_list = request.POST.getlist('items')
        params = request.POST.dict()
        # print(params)

        for id in item_list:
            id = int(id)
            items.append(test_menu[id])

        nutrient = ""
        value = 0
        price = 0

        if params["price"] != '':
            price = float(params["price"])

        if params["carbs"] != '':
            value = int(params["carbs"])
            nutrient = "carbs"
        elif params["protein"] != '':
            value = int(params["protein"])
            nutrient = "protein"
        elif params["fat"] != '':
            value = int(params["fat"])
            nutrient = "fat"
        elif params["calories"] != '':
            value = int(params["calories"])
            nutrient = "calories"

        if nutrient != "":
            items = remove_items_conditionally(items, nutrient, lambda x, y: x > y, limit=5)
            items = sort_items_by_nutrient(items, nutrient, reverse=True)
            items = get_combos_close_to(items, nutrient, value)
            items = compact_combos(items)

        if price != "":
            items = remove_items_conditionally(items, "price", lambda x, y: x <= y, limit=price)


    else:
        for k in test_menu.keys():
            items.append(test_menu[k])

    ctx = {"items": items}

    return render(request, "menu.html", context=ctx)


def order_page(request):
    return render(request, "order.html")
