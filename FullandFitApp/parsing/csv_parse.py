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
        menu_item.set_members_to_csv_row(dictionary)
        menu[i] = menu_item

    return menu
# menu = get_menu_from_csv("static/Menu_CSV/CarlsJr.csv")


