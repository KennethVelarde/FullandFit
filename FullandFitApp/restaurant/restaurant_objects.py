from itertools import combinations
from sys import getsizeof

class Restaurant:
    def __init__(self):
        self.name = None
        self.logopath = None
        self.menu = None

    def to_dict(self):
        restaurant_dict = dict()
        restaurant_dict["name"] = self.name
        restaurant_dict["menu"] = self.menu.to_dictionary_array()
        restaurant_dict["logopath"] = self.logopath

        return restaurant_dict



def filter_items_by_allergens(items: list, allergens: list):

    filtered_items = []

    for item in items:
        item_dict = item.to_dict()

        allergen_free = True

        for allergen in allergens:
            key = "has_" + allergen
            # print("Has Allergen", item_dict[key])
            if item_dict[key]:
                allergen_free = False
                break

        if allergen_free:
            filtered_items.append(item)

    return filtered_items



class Menu:
    def __init__(self, items: dict):
        self.items = items

    def to_dictionary_array(self):
        ids = list(self.items.keys())
        ids.sort()

        menu_array = []

        for id in ids:
            item_dictionary = self.items[id].to_dict()
            item_dictionary["id"] = id
            menu_array.append(item_dictionary)

        return menu_array

    def get_item_by_id(self, id: int):
        return self.items[id]

def get_combos_and_filter(items, nutrient, nutrient_value, filter, pricepoint):
    max_items_per_combo = 5

    combos = []

    items = [item.to_dict() for item in items]

    items = sorted(items, key=lambda k: k["price"])

    a = len(items) - 1

    if a <= 0:
        return []

    cost = items[a]["price"]
    for i in range(1, max_items_per_combo):
        cost += items[a - i]["price"]
        while cost > pricepoint and a - i > 0:
            cost -= items[a]["price"]
            a -= 1
            cost += items[a - i]["price"]
        for item_array in combinations(items[0:a], i + 1):
            combo = get_combo_from_item_array(item_array)
            if filter(combo.get_total_nutrient_value(nutrient), nutrient_value):
                combos.append(combo)

    return combos


def get_combo_from_item_array(item_array):
    menu_items = []
    for i in range(len(item_array)):
        menu_items.append(get_menu_item_from_dictionary(item_array[i]))

    return Combo(menu_items)

def get_restaurant_from_dictionary(dictionary):
    new_restaurant = Restaurant()
    new_restaurant.name = dictionary["name"]

    dictionary_menu = dictionary["menu"]
    menu_items = dict()

    for dictionary_item in dictionary_menu:
        menu_item = MenuItem()
        menu_item.set_members_from_dictionary(dictionary_item)
        menu_items[dictionary_item["id"]] = menu_item

    menu = Menu()

    new_restaurant.menu = menu



def combos_to_array_of_dictionaries(combos):
    combo_array = []

    for combo in combos:
        combo_array.append(combo.to_dictionary_array())

    return combo_array


class Combo:
    def __init__(self, items):
        self.items = items

    def append(self, item):
        self.items.append(item)

    def convert_to_item_dictionary(self, id):
        combo_item = dict()

        combo_item["id"] = id
        combo_item["name"] = ""
        combo_item["price"] = 0
        combo_item["calories"] = 0
        combo_item["carbs"] = 0
        combo_item["protein"] = 0
        combo_item["fat"] = 0
        combo_item["has_egg"] = False
        combo_item["has_milk"] = False
        combo_item["has_shellfish"] = False
        combo_item["has_soy"] = False
        combo_item["has_peanuts"] = False
        combo_item["has_treenuts"] = False
        combo_item["has_wheat"] = False

        for item in self.items:
            combo_item["name"] += "{}|".format(item.name)
            combo_item["price"] += item.price
            combo_item["calories"] += item.calories
            combo_item["carbs"] += item.carbs
            combo_item["protein"] += item.protein
            combo_item["fat"] += item.fat
            combo_item["has_egg"] = combo_item["has_egg"] or item.has_egg
            combo_item["has_milk"] = combo_item["has_milk"] or item.has_milk
            combo_item["has_shellfish"] = combo_item["has_shellfish"] or item.has_shellfish
            combo_item["has_soy"] = combo_item["has_soy"] or item.has_soy
            combo_item["has_peanuts"] = combo_item["has_peanuts"] or item.has_peanuts
            combo_item["has_treenuts"] = combo_item["has_treenuts"] or item.has_treenuts
            combo_item["has_wheat"] = combo_item["has_wheat"] or item.has_wheat

        description = combo_item["name"].split('|')[0:-1]

        if len(description) > 1:
            description[-1] = "and a {}".format(description[-1])

        combo_item["name"] = ", ".join(description)

        return combo_item

    def to_dictionary_array(self):
        array = []

        for item in self.items:
            array.append(item.to_dict())

        return array

    def get_total_nutrient_value(self, nutrient):
        total_nutrients = 0

        for item in self.items:
            total_nutrients += item.get_macronutrients_as_dictionary()[nutrient]

        return total_nutrients


def get_menu_item_from_dictionary(dictionary):
    menu_item = MenuItem()
    menu_item.set_members_from_dictionary(dictionary)

    return menu_item


def compress_combos(combos):
    return [combos[i].convert_to_item_dictionary(i) for i in range(len(combos))]


def compress_combo(combo):
    return combo.convert_to_item_dictionary(0)


def get_combo_from_item_array(item_array):
    menu_items = []

    for dictionary in item_array:
        menu_item = MenuItem()
        menu_item.set_members_from_dictionary(dictionary)
        menu_items.append(menu_item)

    return Combo(menu_items)


class MenuItem:
    def __init__(self):
        self.name = None
        self.price = None
        self.calories = None
        self.carbs = None
        self.protein = None
        self.fat = None
        self.has_egg = False
        self.has_milk = False
        self.has_peanuts = False
        self.has_shellfish = False
        self.has_soy = False
        self.has_treenuts = False
        self.has_wheat = False

    def set_members_from_dictionary(self, dictionary):
        self.name = dictionary["name"]
        self.price = dictionary["price"]
        self.calories = dictionary["calories"]
        self.carbs = dictionary["carbs"]
        self.protein = dictionary["protein"]
        self.fat = dictionary["fat"]
        self.has_egg = dictionary["has_egg"]
        self.has_milk = dictionary["has_milk"]
        self.has_peanuts = dictionary["has_peanuts"]
        self.has_shellfish = dictionary["has_shellfish"]
        self.has_soy = dictionary["has_soy"]
        self.has_treenuts = dictionary["has_treenuts"]
        self.has_wheat = dictionary["has_wheat"]

    def set_members_to_csv_row(self, menu_item_dictionary):
        self.name = menu_item_dictionary["name"].strip()

        self.price = menu_item_dictionary["price"].strip()

        if self.price[0] is '$':
            self.price = float(self.price[1:])
        else:
            self.price = float(self.price)

        self.calories = int(menu_item_dictionary["calories"])
        self.carbs = int(menu_item_dictionary["carbs"])
        self.protein = int(menu_item_dictionary["protein"])
        self.fat = int(menu_item_dictionary["fat"])

        if menu_item_dictionary["egg"] is "1":
            self.has_egg = True
        if menu_item_dictionary["milk"] is "1":
            self.has_milk = True
        if menu_item_dictionary["peanuts"] is "1":
            self.has_peanuts = True
        if menu_item_dictionary["shellfish"] is "1":
            self.has_shellfish = True
        if menu_item_dictionary["soy"] is "1":
            self.has_soy = True
        if menu_item_dictionary["treenuts"] is "1":
            self.has_treenuts = True
        if menu_item_dictionary["wheat"] is "1":
            self.has_wheat = True

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "calories": self.calories,
            "carbs": self.carbs,
            "protein": self.protein,
            "fat": self.fat,
            "has_egg": self.has_egg,
            "has_milk": self.has_milk,
            "has_peanuts": self.has_peanuts,
            "has_shellfish": self.has_shellfish,
            "has_soy": self.has_soy,
            "has_treenuts": self.has_treenuts,
            "has_wheat": self.has_wheat
        }

    def get_macronutrients_as_dictionary(self):

        return {
            "calories": self.calories,
            "carbs": self.carbs,
            "protein": self.protein,
            "fat": self.fat,
        }
