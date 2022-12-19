count_cars = int(input())
all_cars = set()
for _ in range(count_cars):
    action,number_plate = input().split(", ")
    if action == "IN":
        all_cars.add(number_plate)
    elif action == "OUT":
        all_cars.remove(number_plate)

if not all_cars:
    print("Parking Lot is Empty")
else:
    print("\n".join(all_cars))