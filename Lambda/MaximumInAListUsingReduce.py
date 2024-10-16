### 7. Find Maximum in a List Using Lambda

from functools import reduce


def find_max(nums):
    # Find the maximum number in a list
    return reduce(lambda x, y: x if x > y else y, nums)

# Example usage
nums = [1, 2, 3, 4, 5]
print(find_max(nums))
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
reduce
Purpose: Applies a given function cumulatively to the items of an iterable, reducing it to a single value. It is part of the functools module.
Usage: Typically used when you want to combine or aggregate values, such as summing a list or finding a product.
'''

"""
Key Differences
Functionality:

map transforms each element individually.
reduce aggregates elements into a single result.
Return Type:

map returns an iterable of the same length as the input.
reduce returns a single value.
"""