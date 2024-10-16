## 8. Find the Average of a List Using Lambda

from functools import reduce


# nums = [1, 2, 3, 4, 5]

# def avgOfList(l1):
#     return reduce(lambda x,y:x+y//len(l1),nums)
    
# print(avgOfList(nums))
def average(nums):
    # Calculate the average of a list of numbers
    return reduce(lambda x, y: x + y, nums) / len(nums)

# Example usage
nums = [1, 2, 3, 4, 5]
print(average(nums))
# Time Complexity: O(n)
# Space Complexity: O(1)