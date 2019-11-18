import os
from FullandFitApp import nutrition_optimization
from FullandFitApp.restaurant import restaurant_objects
from FullandFitApp import reads

from django.shortcuts import render, redirect
from django.contrib import messages

from FullandFitSite.settings import STATIC_ROOT


IMG_DIR = os.path.join(STATIC_ROOT, "img")


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def restaurants_page(request):
    restaurants_from_db = reads.get_restaurants()

    restaurants = []
    for dictionary in restaurants_from_db:
        restaurant = dict()
        restaurant["thumbnail_filename"] = dictionary["image_path"].split("/")[-1]
        restaurant["name"] = dictionary["name"]
        restaurant["menu_id"] = dictionary["menu_id"]
        restaurants.append(restaurant)

    ctx = {"restaurants": restaurants}

    return render(request, "restaurants.html", context=ctx)


def menu(request, menu_id, restaurant_name):

    # session variables
    current_restaurant = restaurant_objects.Restaurant()
    current_combos = []
    sales_tax = 0

    menu_item_dictionaries = reads.get_menu(menu_id)

    # # todo: convert to draw from database

    # todo: refactor the current restaurant building to another function
    current_restaurant.name = restaurant_name.split('.')[0]
    menu_items = restaurant_objects.get_menu_from_menu_item_dictionaries(menu_item_dictionaries)
    current_restaurant.menu = restaurant_objects.Menu(menu_items)

    items = []

    if request.method == "POST" and request.POST.getlist('items') is not None:

        item_ids = request.POST.getlist('items')
        params = request.POST.dict()

        print(params)

        sales_tax = float(params["sales_tax"]) / 100

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
            price = float(params["price"]) / (1 + sales_tax)

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

        allergens = []
        if params["exclude_egg"] == "true":
            allergens.append("egg")
        if params["exclude_milk"] == "true":
            allergens.append("milk")
        if params["exclude_shellfish"] == "true":
            allergens.append("shellfish")
        if params["exclude_peanuts"] == "true":
            allergens.append("peanuts")
        if params["exclude_soy"] == "true":
            allergens.append("soy")
        if params["exclude_treenuts"] == "true":
            allergens.append("treenuts")
        if params["exclude_wheat"] == "true":
            allergens.append("wheat")

        items = restaurant_objects.filter_items_by_allergens(items, allergens)


        # if price is 0, don't consider it
        if price == 0:
            price += 99999

        if algorithm == "less_than":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = restaurant_objects.get_combos_and_filter(
                    items,
                    nutrient,
                    value,
                    lambda x, y: x <= y,
                    price
                )
                items = restaurant_objects.compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")
        elif algorithm == "exactly":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = restaurant_objects.get_combos_and_filter(
                    items,
                    nutrient,
                    value,
                    lambda x, y: 0.9 * y <= x <= 1.1 * y,
                    price
                )
                items = restaurant_objects.compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")
        elif algorithm == "greater_than":
            if price > 0 and value > 0 and price < 20 and value < 2000:
                current_combos = restaurant_objects.get_combos_and_filter(
                    items,
                    nutrient,
                    value,
                    lambda x, y: x >= y,
                    price
                )
                items = restaurant_objects.compress_combos(current_combos)
            else:
                messages.error(request, "Dollar value must be between $0.01 and $19.99")
                messages.error(request, "Nutrient value must be between 1 and 2000")

        request.session["current_combos"] = restaurant_objects.combos_to_array_of_dictionaries(current_combos)
        request.session["sales_tax"] = sales_tax

        return redirect("combos")
    else:
        items = current_restaurant.menu.to_dictionary_array()

    # make session variables persistent across pages
    request.session["current_restaurant"] = current_restaurant.to_dict()

    ctx = {"restaurant_name": current_restaurant.name, "menu": items}

    return render(request, "menu.html", context=ctx)


def combos_page(request):

    current_combos = request.session["current_combos"]
    current_restaurant = request.session["current_restaurant"]

    combos = [restaurant_objects.get_combo_from_item_array(item_array) for item_array in current_combos]

    compressed_combos = restaurant_objects.compress_combos(combos)

    print(compressed_combos)

    ctx = {"combos": compressed_combos, "restaurant_name": current_restaurant["name"]}

    return render(request, "combos.html", context=ctx)


def order_page(request, combo_id):

    current_combos = request.session["current_combos"]
    sales_tax = request.session["sales_tax"]

    combo = current_combos[combo_id]

    compressed_combo = restaurant_objects.compress_combo(restaurant_objects.get_combo_from_item_array(combo))

    subtotal = compressed_combo["price"]
    total = subtotal + subtotal * sales_tax

    return render(request, "order.html", {"combo": combo, "subtotal": subtotal, "total": total})
