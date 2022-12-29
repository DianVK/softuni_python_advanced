from collections import deque

boxes_with_materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {
    "Bicycle": [0, 400],
    "Doll": [0, 150],
    "Teddy bear": [0, 300],
    "Wooden train": [0, 250]
}

while boxes_with_materials and magic_values:
    material = boxes_with_materials.pop()
    magic = magic_values.popleft()

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_values.appendleft(magic)
        continue
    if magic == 0:
        boxes_with_materials.append(material)
        continue

    product_of_operation = material * magic
    if product_of_operation < 0:
        result = material + magic
        boxes_with_materials.append(result)

    else:
        found_present = False
        for gift, data in presents.items():
            _, magic_level = data
            if magic_level == product_of_operation:
                presents[gift][0] += 1
                found_present = True
                break
        if product_of_operation > 0 and not found_present:
            boxes_with_materials.append(material + 15)

if (presents["Bicycle"][0] >= 1 and presents["Teddy bear"][0] >= 1) or \
        (presents["Doll"][0] >= 1 and presents["Wooden train"][0] >= 1):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in boxes_with_materials[::-1])}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for gift, data in presents.items():
    amount, _ = data
    if amount >= 1:
        print(f"{gift}: {amount}")

# from collections import deque
# materials = deque(int(x) for x in input().split())
# magic_level = deque(int(x) for x in input().split())
# presents = {'150':'Doll','250':'Wooden train', '300':'Teddy bear','400':'Bicycle'}
# count_presents = {}
# presents_value = False
# while (len(count_presents) < len(presents)) and materials and magic_level:
#     last_box = materials.pop()
#     first_magic = magic_level.popleft()
#     result = last_box * first_magic
#     if result > 0:
#         if str(result) in presents:
#             for key,value in presents.items():
#                 if key == str(result):
#                     if value not in count_presents:
#                         count_presents[value] = 1
#                     else:
#                         count_presents[value] += 1
#         else:
#             materials.appendleft(first_magic + 15)
#     elif result < 0:
#         result = last_box + first_magic
#         materials.append(result)
#     elif last_box == 0:
#         magic_level.appendleft(first_magic)
#     elif first_magic == 0:
#         materials.append(last_box)
#     if ('Doll' in count_presents and 'Wooden train' in count_presents) or ('Teddy bear' in count_presents and  'Bicycle' in count_presents):
#         print("The presents are crafted! Merry Christmas!")
#         presents_value = True
#         break
#
# if not presents_value:
#     print("No presents this Christmas!")
# if materials:
#     print(f"Materials left: ",end="")
#     print(*materials,sep=", ")
# if magic_level:
#     print(f"Magic left: ",end="")
#     print(*magic_level,sep=", ")
# for key,value in count_presents.items():
#     print(f"{key}: {value}")