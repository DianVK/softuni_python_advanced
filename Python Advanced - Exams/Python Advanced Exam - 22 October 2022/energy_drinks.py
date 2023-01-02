from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

total_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    current_result = current_caffeine * current_energy_drink
    if current_result + total_caffeine <= 300:
        total_caffeine += current_result
    else:
        energy_drinks.append(current_energy_drink)
        if total_caffeine - 30 < 0:
            total_caffeine = 0
        else:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: ",end="")
    print(*energy_drinks,sep=", ")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")