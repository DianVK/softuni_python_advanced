from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
operations = deque(input().split())

honey_made = 0
operators = {
    "+": lambda f, s: f + s,
    "-": lambda f, s: f - s,
    "*": lambda f, s: f * s,
    "/": lambda f, s: f / s
}

while bees and nectar:
    bee = bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar < bee:
        bees.appendleft(bee)
        continue
    operation = operations.popleft()
    if last_nectar > 0:
        honey_made += abs(operators[operation](bee, last_nectar))

print(f"Total honey made: {honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")