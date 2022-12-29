first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()

    if "Check Subset" not in command:
        numbers = [int(x) for x in command.split() if x.isdigit()]

        if "First" in command:
            if "Add" in command:
                for num in numbers:
                    first_set.add(num)

            elif "Remove" in command:
                for num in numbers:
                    first_set.discard(num)

        elif "Second" in command:
            if "Add" in command:
                for num in numbers:
                    second_set.add(num)

            elif "Remove" in command:
                for num in numbers:
                    second_set.discard(num)

    else:
        print(first_set.issuperset(second_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")