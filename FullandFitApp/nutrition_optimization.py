from FullandFitApp.restaurant import restaurant_objects

#
# def unbounded_knapsack(v, w, cap):
#     n = len(v)
#     sack = [0] * (cap + 1)
#     items = [-1] * (cap + 1)
#     solutions = dict()
#
#     for j in range(1, cap + 1):
#         items[j] = items[j - 1]
#         solutions[j] = []
#         max = sack[j - 1]
#         for i in range(n):
#             x = j - w[i]
#             if x >= 0 and sack[x] + v[i] >= max:
#                 max = sack[x] + v[i]
#                 items[j] = i
#                 solutions[j].append(i)
#             sack[j] = max
#     return sack[cap]
#
# # todo: remove all items from the list over 110% of the queried value
# def get_target(items, nutrient, value, price):
#     items = remove_items_conditionally(items, nutrient, lambda x, y: x > y, critical_value=5)
#     items = sort_items_by_nutrient(items, nutrient, reverse=True)
#     items = [item.to_dict() for item in items]
#
#     combos = get_combos_close_to(items, nutrient, value, price)
#
#     for i in range(len(combos)):
#         for j in range(len(combos[i].items)):
#             item = combos[i].items[j]
#             combos[i].items[j] = restaurant_objects.get_menu_item_from_dictionary(item)
#
#     return combos
#     # items = compact_combos(items)
#     # items = remove_items_conditionally(items, nutrient, lambda x, y: x <= y, critical_value=(1.1 * value))
#
#
# def get_max(items, nutrient, pricepoint):
#
#     # convert pricepoint to cents
#     pricepoint *= 100
#     pricepoint = int(pricepoint)
#
#     # construct an array of weights and an array of values
#     w = []
#     v = []
#     for item in items:
#         v.append(item[nutrient])
#
#         # convert price to cents
#         price = item["price"]
#         price *= 100
#         price = int(price)
#
#         w.append(price)
#
#     # get the maximum possible value from the two arrays
#     maximum = unbounded_knapsack(v, w, pricepoint)
#
#     return get_target(items, nutrient, maximum, pricepoint)
#
#
# def compact_description(description):
#     """
#     compact a list of words in string format into a counted
#     list
#
#     e.g. hotdog hotdog hotdog fries fries becomes 3 hotdogs and 2 fries
#
#     :param description: list of words in string format
#     :return: counted list in string format
#     """
#
#     # dictionary to hold word counts
#     # { "word" : # of occurences }
#     d = dict()
#
#     # split the string into a list based on the delimiter
#     # set in the get combos function
#     description = description.strip().split('|')
#
#     # count each word by incrementing the appropriate
#     # counter in the dictionary
#     for word in description:
#         # if the word does not exist as a key then create it
#         try:
#             d[word] += 1
#         except KeyError:
#             d[word] = 1
#
#     # container string for final output
#     description = ""
#
#     # retrieve the words from the dictionary
#     keys = list(d.keys())
#
#     # place the words into the string with the counts
#     for i in range(len(keys)):
#         amount = d[keys[i]]
#         item = keys[i]
#
#         # add an s if the string needs to be plural
#         # and an s is not already at the end of the word
#         if amount > 1 and item[-1] != 's':
#             item += 's'
#
#         # add an and if more than 1 mord exists
#         if len(keys) > 1 and i == len(keys) - 1:
#             description += " and "
#
#         # build the output string
#         description += "{} {}\n".format(amount, item)
#
#     return description
#
#
# def compact_combos(combos):
#     """
#     compact combos (lists of items) into a single item
#     to represent the combo
#     :param combos: a list of list of dictionaries
#     :return:  a list of dictionaries
#     """
#
#     # output container
#     compact_combos = []
#
#     # cycle through each combo and compact it
#     for combo in combos:
#
#         # container for the final combo item
#         compact_combo = dict()
#
#         # instantiate the dictionary keys
#         compact_combo["name"] = ""
#         compact_combo["price"] = 0
#         compact_combo["calories"] = 0
#         compact_combo["carbs"] = 0
#         compact_combo["protein"] = 0
#         compact_combo["fat"] = 0
#
#         # string to hold the items as list in string format
#         item_list = ""
#
#         # add all the items in a combo together
#         for item in combo:
#             item_list += "{}|".format(item["name"].strip())
#             compact_combo["price"] += item["price"]
#             compact_combo["calories"] += item["calories"]
#             compact_combo["carbs"] += item["carbs"]
#             compact_combo["protein"] += item["protein"]
#             compact_combo["fat"] += item["fat"]
#
#         # trim the final | delimiter off the end of the item list
#         item_list = item_list[0:-1]
#
#         # compact the item list into a combo description
#         compact_combo["name"] = compact_description(item_list)
#
#         # add the combo to the list of combos
#         compact_combos.append(compact_combo)
#
#     return compact_combos
#
#
# def sort_items_by_nutrient(items, nutrient, reverse=False):
#     """
#     Function: Sort a list of items by the given
#               nutrient
#     :param items: a list of dictionaries
#     :param nutrient: a string corresponding to a key
#                      in the item dictionaries
#     :param reverse: sort in ascending order if true and
#                     descending if false
#     :return: the list of items sorted by the nutrient
#     """
#
#     item_dicts = [item.to_dict() for item in items]
#     sorted_items = sorted(item_dicts, key=lambda k: k[nutrient], reverse=reverse)
#
#     for i in range(len(sorted_items)):
#         item = sorted_items[i]
#         sorted_items[i] = restaurant_objects.get_menu_item_from_dictionary(item)
#
#     return sorted_items
#
#
#
# def remove_items_conditionally(items, key, conditional_function, critical_value=0):
#     """
#     remove items from the list that make the comparator function true
#     comp = lambda x, y: x <some condition> y
#
#     :param items: list of dictionaries
#     :param conditional_function: conditional function for deciding exclusion
#     :param key: value of dictionary to perform comparison
#     :return: list of dictionaries minus the dictionaries matching the comparator function
#     """
#
#     # create container for modified item list
#     new_items = []
#
#     # test each item for exclusion
#     for item in items:
#         item = item.to_dict()
#
#         # if the items value is acceptable then
#         # add it to the output items
#         if conditional_function(item[key], critical_value):
#             new_items.append(restaurant_objects.get_menu_item_from_dictionary(item))
#
#     return new_items
#
#
# def get_combos_close_to(items, nutrient, value, pricepoint):
#     """
#     Function: return the combinations of items close to the
#     specified nutrient value
#     :param items:    a list of dictionaries
#     :param nutrient: a string corresponding to a key in the
#                      item dictionaries
#     :param value:    the target value of the nutrient
#     :return:         a list of lists of dictionaries (the combos)
#     """
#
#     # how many of the current items to add
#     count = 0
#
#     # cost of the items thus far
#     cost = 0
#
#     # the combos that fall around the target value
#     combos = []
#
#     # if no items exist then no combos can be made
#     if len(items) == 0:
#         return []
#
#     # BASE CASE
#     #
#     # if items contains a single item then make a combo
#     # of nothing but that item and return combos
#     if len(items) == 1:
#
#         # container for the created combo
#         new_combo = []
#
#         # add the item until the combo reaches the desired value
#         while count * items[0][nutrient] < value:
#             new_combo.append(items[0])
#
#             cost += items[0]["price"]
#             count += 1
#
#             if cost > pricepoint:
#                 return []
#
#         # add the created combo
#         combos.append(restaurant_objects.Combo(new_combo))
#
#         return combos
#
#     # the combinations of items for count = n is [item * count] +
#     # the combinations made from items other than this item minus the
#     # total value that the items added
#     while count * items[0][nutrient] <= value and cost < pricepoint:
#
#         # calculate the solution combos that are possible at the value minus how many
#         # of the current item you wish to add
#         c = get_combos_close_to(items[1:], nutrient, value - count * items[0][nutrient], pricepoint - cost)
#
#         # add the current item to the calculated combos equal to the current items
#         # you wish to add
#         for i in range(count):
#             for j in range(len(c)):
#                 c[j].append(items[0])
#
#         # add the calculated combos to the total combos thus far
#         for combo in c:
#             combos.append(combo)
#
#         # calculate again with one more of this item
#         count += 1
#         cost += items[0]["price"]
#
#     # for i in range(len(combos)):
#     #     for j in range(len(combos[i])):
#
#     return combos
