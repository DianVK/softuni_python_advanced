from collections import deque
price_per_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence = int(input())
total_sum_spend = 0
barrel_counter,bullets_counter = 0, 0
while bullets and locks:
    total_sum_spend += price_per_bullet
    current_bullet = bullets.pop()
    current_lock = locks[0]
    barrel_counter += 1
    bullets_counter += 1
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    elif current_bullet > current_lock:
        print("Ping!")
    if barrel_counter == size_of_gun_barrel and bullets:
        print("Reloading!")
        barrel_counter = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - total_sum_spend}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")