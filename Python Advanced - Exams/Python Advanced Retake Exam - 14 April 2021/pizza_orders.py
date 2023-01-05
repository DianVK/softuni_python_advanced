from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees_capacity = [int(x) for x in input().split(", ")]

pizzas_made = 0

while orders and employees_capacity:
    current_order = orders.popleft()
    current_employee = employees_capacity.pop()
    if current_order > 10:
        employees_capacity.append(current_employee)
    elif current_order <= 0:
        employees_capacity.append(current_employee)
    elif current_employee >= current_order:
        pizzas_made += current_order
    elif current_order > current_employee:
        order_left = current_order - current_employee
        pizzas_made += current_employee
        orders.appendleft(order_left)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}\nEmployees: ",end="")
    print(*employees_capacity, sep=", ")

if not employees_capacity and orders:
    print("Not all orders are completed.\nOrders left: ",end="")
    print(*orders, sep=", ")