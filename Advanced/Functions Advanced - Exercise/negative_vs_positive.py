def negative_vs_positive(nums):
    positives = list([0])
    negatives = list([0])
    result = [positives.append(num) if num > 0 else negatives.append(num) for num in nums]
    bigger_list = "positives" if sum(positives) > abs(sum(negatives)) else "negatives"
    smaller_list = "negatives" if sum(positives) > abs(sum(negatives)) else "positives"
    return f"{sum(negatives)}\n{sum(positives)}\nThe {bigger_list} are stronger than the {smaller_list}"


numbers = [int(x) for x in input().split()]
print(negative_vs_positive(numbers))