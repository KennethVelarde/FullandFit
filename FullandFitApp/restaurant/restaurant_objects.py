class Restaurant:
    def __init__(self):
        self.name = None
        self.logopath = None
        self.menu = None
        self.csvfile = None

    def get_menu_item_dictionary_array(self):
        menu_array = []
        for menu_item in self.menu:
            menu_array.append(menu_item.to_dict())

        return menu_array


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

    def set_members_by_dictionary(self, menu_item_dictionary):
        self.name = menu_item_dictionary["name"]

        self.price = menu_item_dictionary["price"]

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

