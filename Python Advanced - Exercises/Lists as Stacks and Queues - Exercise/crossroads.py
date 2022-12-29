from _collections import deque
green_light_time = int(input())
window_time = int(input())
data = input()

all_cars = deque()
cars_counter = 0
crashed = False

while data != "END":
    if data == "green":
        if all_cars:
            current_car = all_cars.popleft()
            left_seconds = green_light_time - len(current_car)

            while left_seconds > 0:
                cars_counter += 1
                if not all_cars:
                    break
                current_car = all_cars.popleft()
                left_seconds -= len(current_car)

            if left_seconds == 0:
                cars_counter += 1
            if window_time >= abs(left_seconds):
                if left_seconds < 0:
                    cars_counter += 1
            else:
                index = window_time + left_seconds
                print(f"A crash happened!\n{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        all_cars.append(data)
    data = input()

if not crashed:
    print(f"Everyone is safe.\n{cars_counter} total cars passed the crossroads.")