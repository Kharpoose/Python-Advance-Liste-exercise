def union_intersection(lst1, lst2):
    
    union = list(set(lst1) | set(lst2))
    intersection = list(set(lst1) & set(lst2))
    
    return union, intersection 


nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7, 8]

print(union_intersection(nums1, nums2))

result = union_intersection(nums1, nums2)

print("Union of the list:")
print(result[0])

print("intersection of the list: ")
print(result[1])