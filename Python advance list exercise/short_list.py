from heapq import heapify, heappush, heappop

def short_list(nums):
    heap_lst = []
    
    heapify(heap_lst)
    
    for lst in nums:
        for val in lst:
            heappush(heap_lst, val)
            
    return [heappop(heap_lst) for _ in range(len(heap_lst))]       

nums = [[1, 4, 5], [1, 3, 4], [2, 6, 7, 8]]


print("Original list:")
print(nums)

result = short_list(nums)

print("Merge k Sorted Lists into a list:")
print(result)
