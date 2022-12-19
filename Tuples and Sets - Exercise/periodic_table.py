count_input_lines = int(input())
all_items = set()
for _ in range(count_input_lines):
    chemical_compounds = input().split()
    for item in chemical_compounds:
        if len(item)>1:
            item = item.split()
            for x in item:
                all_items.add(x)
        else:
            all_items.add(item)

print(*all_items,sep="\n")