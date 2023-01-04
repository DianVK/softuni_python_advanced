from collections import deque


def check_gifts(s,material,magic):
    global gemstone,porcelain_sculpture,gold,diamond_jewellery
    if 100 > s:
        if s % 2 == 0:
            material = material * 2
            magic = magic * 3
            s = material + magic
        else:
            material = material * 2
            magic = magic * 2
            s = material + magic
    elif s >= 500:
        s = s / 2
    if 100 <= s < 200:
        gemstone += 1
    elif 200 <= s < 300:
        porcelain_sculpture += 1
    elif 300 <= s < 400:
        gold += 1
    elif 400 <= s < 500:
        diamond_jewellery += 1


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    current_sum = current_magic + current_material
    check_gifts(current_sum, current_material, current_magic)

if (gemstone != 0 and porcelain_sculpture != 0) or (gold != 0 and diamond_jewellery != 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print("Materials left: ",end="")
    print(*materials,sep=", ")
elif magic_levels:
    print("Magic left: ",end="")
    print(*magic_levels,sep=", ")
if gemstone != 0:
    print(f"Gemstone: {gemstone}")
if porcelain_sculpture != 0:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")
if gold != 0:
    print(f"Gold: {gold}")
if diamond_jewellery != 0:
    print(f"Diamond Jewellery: {diamond_jewellery}")