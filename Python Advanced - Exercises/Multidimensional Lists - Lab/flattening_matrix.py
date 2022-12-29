rows = int(input())
matrix = []

for i in range(rows):
    nums = input().split(", ")
    for num in range(len(nums)):
        nums[num] = int(nums[num])
        matrix.append(nums[num])

print(matrix)