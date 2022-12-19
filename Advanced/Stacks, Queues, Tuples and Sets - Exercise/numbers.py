first_seq = (int(x) for x in input().split())
second_seq = (int(x) for x in input().split())
count_lines = int(input())
for _ in range(count_lines):
    command = input().split()
    current_action = command[0]
    action_num = command[1]
    if current_action == "Add ":
        if action_num == "First":
        elif action_num == "Second":
    elif current_action == "Remove ":
        if action_num == "First":
        elif action_num == "Second":
    elif current_action == "Check ":