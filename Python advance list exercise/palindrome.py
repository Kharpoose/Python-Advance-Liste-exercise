def is_palindrome(lst):
    return lst == lst[::-1]

nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

print("Original list:")
print(nums)

print("Check the said list is Palindrome or not?")
print(is_palindrome(nums))

nums = [1, 2, 2, 1]

print("Original list:")
print(nums)

print("Check the said list is Palindrome or not?")
print(is_palindrome(nums))