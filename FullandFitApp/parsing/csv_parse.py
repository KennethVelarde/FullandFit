import csv
from FullandFitApp.restaurant.restaurant_objects import *

def get_headers_and_rows_from_csv(filepath):
    headers = []
    rows = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)

        header_row = True
        for line in reader:
            if header_row:
                headers = line
                header_row = False
                continue
            rows.append(line)

    return headers, rows


def convert_headers_and_rows_to_dictionaries(headers, rows):
    dictionaries = []
    header_count = len(headers)

    for row in rows:
        new_dict = dict()
        for i in range(header_count):
            new_dict[headers[i].strip()] = row[i]
        dictionaries.append(new_dict)

    return dictionaries


def get_menu_from_csv(filepath):
    menu = dict()
    headers, rows = get_headers_and_rows_from_csv(filepath)
    item_dictionaries = convert_headers_and_rows_to_dictionaries(headers, rows)

    for i in range(len(item_dictionaries)):
        dictionary = item_dictionaries[i]

        # only consider menu items that have a price
        if dictionary["price"] is "":
            continue

        menu_item = MenuItem()
        menu_item.set_members_by_dictionary(dictionary)
        menu[i] = menu_item

    return menu
# menu = get_menu_from_csv("static/Menu_CSV/CarlsJr.csv")


def read_menu(csv_file_name):
    menu = []
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)

        id = 0
        skip_header = True
        for line in reader:

            if skip_header:
                skip_header = False
                continue

            item = dict()
            item["name"] = line[0]
            item["id"] = id
            item["price"] = line[1].strip()

            if len(item["price"]) == 0:
                continue

            if item["price"][0] == '$':
                item["price"] = item["price"][1:]

            try:
                item["price"] = float(item["price"])
            except ValueError:
                continue

            item["calories"] = int(line[2])
            item["carbs"] = int(line[3])
            item["protein"] = int(line[4])
            item["fat"] = int(line[5])

            menu.append(item)

            id += 1

    return menu
