def reverse_list_selected_location(lst, start, end):
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        
        start += 1
        end -= 1
        
    return lst


nums = [10, 20, 30, 40, 50, 60, 70, 80]    

selected_start = 2
selected_end = 5

print("Original List")
print(nums)

print("After Change")
print(reverse_list_selected_location(nums, selected_start, selected_end))