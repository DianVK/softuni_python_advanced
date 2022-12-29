from collections import deque
cups_capacity = deque(int(x) for x in input().split())
filled_bottles = [int(x) for x in input().split()]
wasted_litters = 0
while cups_capacity and filled_bottles:
    current_bottle = filled_bottles.pop()
    if current_bottle >= cups_capacity[0]:
        wasted_litters += current_bottle - cups_capacity[0]
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= current_bottle

if not cups_capacity:
    print("Bottles: ",end="")
    print(*filled_bottles)
if not filled_bottles:
    print("Cups: ",end="")
    print(*cups_capacity)

print(f"Wasted litters of water: {wasted_litters}")
