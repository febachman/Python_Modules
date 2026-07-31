#!/usr/bin/env python3

import sys


def parse_inventory(args: list) -> dict:
    inventory = {}
    for arg in args:
        colon_pos = -1
        for i in range(len(arg)):
            if arg[i] == ':':
                colon_pos = i
                break
        if colon_pos == -1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item = arg[:colon_pos]
        raw_quantity = arg[colon_pos + 1:]
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            int_quantity = int(raw_quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inventory[item] = int_quantity
    return dict(inventory)


def inventory_analyst(inventory: dict) -> None:
    print(f"Got inventory: {inventory}")
    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")
    items_total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {items_total}")
    for item, amount in inventory.items():
        percentage = round((amount / items_total) * 100, 1)
        print(f"Item {item} represents {percentage}%")
    most_item = ""
    most_amount = -1
    least_item = ""
    least_amount = -1
    for item, amount in inventory.items():
        if most_amount == -1 or amount > most_amount:
            most_amount = amount
            most_item = item
        if least_amount == -1 or amount < least_amount:
            least_amount = amount
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {most_amount}")
    print(f"Item least abundant: {least_item} with quantity {least_amount}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main():
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    inventory_analyst(inventory)


if __name__ == "__main__":
    main()
