from collections import deque
number_lines = int(input())
stack_queries = deque()
for _ in range(number_lines):
    command = input()
    if command == "2":
        if stack_queries:
            stack_queries.pop()
    elif command == "3":
        print(max(stack_queries))
    elif command == "4":
        print(min(stack_queries))
    else:
        command,number = command.split()
        stack_queries.append(int(number))
stack_queries = (deque(reversed(stack_queries)))
print(*stack_queries,sep=", ")