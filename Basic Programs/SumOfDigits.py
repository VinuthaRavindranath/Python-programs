## 20. To Find Sum of Digits in a Number (While Loop)
def sum_of_digits(num):
    """
    Find the sum of the digits in a number.
    
    Parameters:
    n (int): The number to process.
    
    Returns:
    int: The sum of the digits.
    
    Time Complexity: O(d), where d is the number of digits.
    Space Complexity: O(1)
    """
    total = 0
    while num > 0:
        total += num % 10
        num =num // 10
    return total

# Example usage
print(sum_of_digits(12345))  # Output: 15

#or

def sum_of_digits(n):
    total = sum(int(digit) for digit in str(n))
    return total

print(sum_of_digits(12345)) 