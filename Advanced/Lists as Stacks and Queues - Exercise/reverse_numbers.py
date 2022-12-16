from collections import deque
numbers = deque(input().split())

while numbers:
    print(numbers.pop(),end=" ")