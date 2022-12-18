from collections import deque
green_light_dur = int(input())
free_window_dur = int(input())
data = input()
cars_counter = 0
all_cars = deque()
crash = False

while data != "END":
    if data == "green":
        if all_cars:
            current_car = all_cars.popleft()
            left_seconds = green_light_dur - len(current_car)
            while left_seconds > 0:
                cars_counter += 1
                if not all_cars:
                    break
                current_car = all_cars.popleft()
                left_seconds -= len(current_car)

            if left_seconds == 0:
                cars_counter += 1
            if free_window_dur >= abs(left_seconds):
                if left_seconds < 0:
                    cars_counter += 1
            else:
                index = free_window_dur + left_seconds
                print(f"A crash happened!\n{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
        else:
            all_cars.append(data)
        line = input()

        if not free_window_dur:
            print(f"Everyone is safe.\n{cars_counter} total cars passed the crossroads.")
