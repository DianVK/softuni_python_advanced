from collections import deque
count_gas_stations = int(input())
gas_stations = deque()

for fueling in range(count_gas_stations):
    gas_stations.append([int(x) for x in input().split()])

for trip in range(count_gas_stations):
    full_trip = True
    tank = 0
    for fuel,distance in gas_stations:
        tank += fuel
        if tank < distance:
            full_trip = False
            break
        else:
            tank -= distance
    if full_trip:
        print(trip)
        break
    else:
        gas_stations.append(gas_stations.popleft())


