from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


def restaurants_page(request):
    return render(request, "restaurants.html")


def menu_page(request):

    # make database selection
    test_menu = dict()
    test_menu[0] = {"id": 0, "name": "burger", "price": 5.99, "calories": 700, "carbs": 60, "protein": 30, "fat": 10}
    test_menu[1] = {"id": 1, "name": "fries", "price": 2.50, "calories": 100, "carbs": 10, "protein": 0, "fat": 15}

    items = []

    if request.method == "POST":
        item_list = request.POST.getlist('items')
        print(request.POST.dict())
        for id in item_list:
            id = int(id)
            items.append(test_menu[id])

    else:
        for k in test_menu.keys():
            items.append(test_menu[k])


    ctx = {"items": items}

    return render(request, "menu.html", context=ctx)


def order_page(request):
    return render(request, "order.html")
