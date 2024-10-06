def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

nums = [54, 657, 314, 546, 1]
result = sum_of_list(nums)
print(f"{result}")