from collections import OrderedDict

def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))


nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

print("Original list:")
print(nums)

result = remove_duplicates(nums)

print("Remove duplicates from the said list while preserving the order:")
print(result)