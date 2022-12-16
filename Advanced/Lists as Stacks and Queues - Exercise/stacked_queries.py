count_commands = int(input())
stack_queries = []


def check_stack_size():
    if len(stack_queries) != 0:
        return True


for _ in range(count_commands):
    command = input()
    if command.startswith("1"):
        __, number = command.split()
        stack_queries.append(int(number))
    elif check_stack_size():
        if command.startswith("2"):
            stack_queries.pop()
        elif command.startswith("3"):
            print(max(stack_queries))
        elif command.startswith("4"):
            print(min(stack_queries))

print(", ".join(str(stack_queries.pop()) for n in range(len(stack_queries))))