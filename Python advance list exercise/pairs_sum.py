def pairs_with_sum(lst, g_sum):

    complement_dict = {}

    pairs = []
    
    for num in lst:
        
        if g_sum - num in complement_dict:
            
            pairs.append((num, g_sum - num))
            
        else:
            
            complement_dict[num] = g_sum - num
            
    return pairs


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 10

print("Original list:")
print(nums)

result = pairs_with_sum(nums, val)

print("List all pairs of the said list whose sum equals to", val)
print(result)
