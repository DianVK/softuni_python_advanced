from collections import deque
food_quantity = int(input())
quantity_food_each_order = deque(int(num) for num in input().split())
print(max(quantity_food_each_order))

while food_quantity != 0 or quantity_food_each_order:
    current_order = quantity_food_each_order.popleft()
    if food_quantity == 0 or not quantity_food_each_order:
        print("Orders complete")
        break
    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        quantity_food_each_order.appendleft(current_order)
        print("Orders left:", *quantity_food_each_order)
        break