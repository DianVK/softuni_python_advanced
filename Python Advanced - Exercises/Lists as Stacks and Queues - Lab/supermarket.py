from collections import deque

customers = deque()

while True:
    command = input()
    if command == "Paid":
        while len(customers):
            print(customers.popleft())
    elif command == "End":
        print(f"{len(customers)} people remaining.")
        break
    else:
        customers.append(command)