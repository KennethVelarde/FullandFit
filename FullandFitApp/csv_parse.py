import csv


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
            item["price"] = line[1]

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
