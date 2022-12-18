from collections import deque
sequence = deque(input())
balanced = False
while sequence:
    left = sequence.popleft()
    right = sequence.pop()
    if left == "(" and right == ")":
        balanced = True
    elif left == "{" and right == "}":
        balanced = True
    elif left == "[" and right == "]":
        balanced = True
    else:
        balanced = False
        break
if balanced:
    print("YES")
else:
    print("NO")