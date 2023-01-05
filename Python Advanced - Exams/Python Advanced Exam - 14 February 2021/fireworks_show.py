from collections import deque

fireworks = deque(int(x) for x in input().split(", "))
explosive = [int(x) for x in input().split(", ")]

count_palm = 0
count_willow = 0
count_crossette = 0
perfect_show = False

while fireworks and explosive:
    current_firework = int(fireworks.popleft())
    current_explosive = int(explosive.pop())
    if current_firework <= 0 or current_explosive <= 0:
        if current_firework <= 0:
            explosive.append(current_explosive)
        if current_explosive <=0:
            fireworks.appendleft(current_firework)
    else:
        values_sum = current_explosive + current_firework
        if values_sum % 3 == 0 and values_sum % 5 != 0:
            count_palm += 1
        elif values_sum % 3 != 0 and values_sum % 5 == 0:
            count_willow += 1
        elif values_sum % 3 == 0 and values_sum % 5 == 0:
            count_crossette += 1
        else:
            current_firework -= 1
            fireworks.append(current_firework)
            explosive.append(current_explosive)
        if count_palm >= 3 and count_willow >= 3 and count_crossette >= 3:
            perfect_show = True

if perfect_show:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: ",end="")
    print(*fireworks,sep=", ")
if explosive:
    print(f"Explosive Power left: ",end="")
    print(*explosive,sep=", ")
print(f"Palm Fireworks: {count_palm}\nWillow Fireworks: {count_willow}\nCrossette Fireworks: {count_crossette}")