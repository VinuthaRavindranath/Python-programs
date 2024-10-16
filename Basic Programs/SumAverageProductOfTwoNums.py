### 2. Sum, Average, and Product of Two Numbers

def sum_average_product(a, b):
    """
    Calculate the sum, average, and product of two numbers.
    
    Parameters:
    a (int or float): First number.
    b (int or float): Second number.
    
    Returns:
    tuple: (sum, average, product)
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    total = a + b
    average = total / 2
    product = a * b
    return total, average, product

# Example usage
print(sum_average_product(4, 6))  # Output: (10, 5.0, 24)