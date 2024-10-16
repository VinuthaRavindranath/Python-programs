### 3. Sum, Average, and Product of a List of Numbers
def sum_average_product_list(numbers):
    """
    Calculate the sum, average, and product of a list of numbers.
    
    Parameters:
    numbers (list): List of numbers.
    
    Returns:
    tuple: (sum, average, product)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    product = 1
    for num in numbers:
        product *= num
    return total, average, product

# Example usage
print(sum_average_product_list([1, 2, 3, 4, 5]))