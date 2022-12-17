from collections import deque
petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    pump_info = [int(x) for x in input().split()]
    pumps.append(pump_info)


for attempt in range(petrol_pumps):
    tank = 0
    full_circle = True
    for petrol, distance in pumps:
        tank += petrol
        if distance > tank:
            full_circle = False
            break
        else:
            tank -= distance
    if full_circle:
        print(attempt)
        break
    else:
        pumps.append(pumps.popleft())