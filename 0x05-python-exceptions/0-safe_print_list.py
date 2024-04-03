#!/usr/bin/python3

def print_items_safely(my_list=[], x=0):
    items_printed = 0
    for i in range(x):
        try:
            print("[{}]".format(my_list[i]), end=", ")
            items_printed += 1
        except IndexError:
            continue
    print("\n Total items printed:", items_printed)
    return items_printed
