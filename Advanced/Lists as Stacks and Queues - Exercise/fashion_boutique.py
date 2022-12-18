from collections import deque
clothes = deque(int(x) for x in input().split())
capacity = int(input())
current_sum = capacity
count_racks = 1

while clothes:
    current_item = clothes.pop()
    if current_sum - current_item >= 0:
        current_sum -= current_item
    else:
        count_racks += 1
        current_sum = capacity
        current_sum -= current_item

print(count_racks)
