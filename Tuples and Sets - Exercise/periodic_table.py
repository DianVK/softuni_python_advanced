count_input_lines = int(input())
unique_compounds = set()
for _ in range(count_input_lines):
    chemical_compounds = input().split()
    for item in chemical_compounds:
        if len(item)>1:
            item = item.split()
            for x in item:
                unique_compounds.add(x)
        else:
            unique_compounds.add(item)

print(*unique_compounds, sep="\n")