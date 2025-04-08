list_items = [
    'a', 's', 132, [725]
]


for items in list_items:
    if isinstance(items, str):
        print(items, isinstance(items, str))

    elif isinstance(items, (int, float)):
        print(items, isinstance(items, (int, float)))
    else:
        print(items)