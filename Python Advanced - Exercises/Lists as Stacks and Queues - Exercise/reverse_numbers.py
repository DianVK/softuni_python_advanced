from collections import deque

numbers = deque([int(x) for x in input().split()])

while numbers:
    print(numbers.pop(),end=" ")