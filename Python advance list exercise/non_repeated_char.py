def first_non_repeated(lst):
    ctr = {}
    for i in lst:
        if i in ctr:
            ctr[i] += 1
            
        else:
            ctr[i] = 1
            
    for i in lst:
        if ctr[i] == 1:
            return i
        
        
nums =  [1, 2, 3, 4, 1, 2, 4, 8]

print("Original list:")
print(nums)

result = first_non_repeated(nums)

print("First non-repeated element in the said list:")
print(result)                        