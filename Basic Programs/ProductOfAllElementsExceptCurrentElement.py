## 47. Calculate the product of all elements in the list except the current element.list1 =[1,2,3,4] -> [24,12,8,6]

def product_except_self(nums):
    """
    Calculate the product of all elements in the list except the current element.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A new list where each element is the product of all other elements in the input list.

    Time Complexity: O(n), where n is the number of elements in the input list.
    Space Complexity: O(1), if we do not consider the output list, as we are using a constant amount of space.
                      If we consider the output list, it is O(n).
    """
    # Calculate the total product
    total_product = 1
    for num in nums:
        total_product *= num

    # Create a new list with the product except self
    result = [total_product // num for num in nums]
    
    return result

# Example usage
list1 = [1, 2, 3, 4]
output = product_except_self(list1)
print(output)  # Output: [24, 12, 8, 6]
