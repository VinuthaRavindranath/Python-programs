## 4. Square of Each Number in a List

def square_numbers(nums):
    # Return the squares of each number in the list
    return list(map(lambda x: x**2, nums))

# Example usage
nums = [1, 2, 3, 4]
print(square_numbers(nums))
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
You use the map() function whenever you want to modify every value in an iterable.

map(function, iterable)
'''