### 6. Reverse a Number
def reverse_number(num):
    """
    Reverse a given number.
    
    Parameters:
    num (int): The number to reverse.
    
    Returns:
    int: The reversed number.
    
    Time Complexity: O(d), where d is the number of digits.
    Space Complexity: O(1)
    """
    reversed_num = 0
    while num > 0:
         digit = num % 10
         reversed_num = reversed_num * 10 + digit
         num=num// 10
    return reversed_num

# Example usage
print(reverse_number(12345))  # Output: 54321