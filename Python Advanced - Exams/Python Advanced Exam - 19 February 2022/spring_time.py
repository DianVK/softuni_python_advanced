def start_spring(**kwargs):
    result = ""
    items_types = {}

    for key, value in kwargs.items():
        if value not in items_types:
            items_types[value] = []
        items_types[value].append(key)

    sorted_items = sorted(items_types.items(), key=lambda x: (-len(x[1]), x[0]))

    for x in sorted_items:
        type_item = x[0]
        items_list = x[1]
        sorted_list_items = sorted(items_list)
        result += f"{type_item}:\n"
        for y in sorted_list_items:
            result += f"-{y}\n"

    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
