from collections import deque
clothes = deque(int(x) for x in input().split())
capacity_per_rack = int(input())
current_sum = capacity_per_rack
count_racks = 1
while clothes:
    current_item = clothes.pop()
    if current_item <= current_sum:
        current_sum -= current_item
    else:
        count_racks += 1
        current_sum = capacity_per_rack
        current_sum -= current_item

print(count_racks)