def reverse_list(items):
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items

nums = [34,6745,578,1,65]
result = reverse_list(nums)
print(f"{result}")
