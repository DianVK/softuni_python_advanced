count_names = int(input())
all_names = set()
for _ in range(count_names):
    name = input()
    all_names.add(name)

print("\n".join(all_names))

# count_names = int(input())
# all_names = {}
# for _ in range(count_names):
#     name = input()
#     if name not in all_names:
#         all_names[name] = 1
#     elif name in all_names:
#         all_names[name] += 1
#
# for key in all_names.items():
#     print(key)