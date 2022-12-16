from collections import deque

dispenser_quantity = int(input())
person = input()

water_line = deque()


def refill(liters):
    global dispenser_quantity
    dispenser_quantity += liters


def get_water(liters):
    global dispenser_quantity
    if liters <= dispenser_quantity:
        dispenser_quantity -= liters
        print(f"{water_line.popleft()} got water")
    else:
        print(f"{water_line.popleft()} must wait")


while person != "Start":
    water_line.append(person)
    person = input()

command = input()
while command != "End":
    if command.isdigit():
        get_water(int(command))
    else:
        _, litters_to_refill = command.split()
        refill(int(litters_to_refill))
    command = input()

print(f"{dispenser_quantity} liters left")