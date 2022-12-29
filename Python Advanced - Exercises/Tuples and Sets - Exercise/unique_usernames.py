count_usernames = int(input())
unique_usernames = set()
for _ in range(count_usernames):
    username = input()
    unique_usernames.add(username)
print("\n".join(unique_usernames))
