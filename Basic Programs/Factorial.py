### 4. Factorial using For Loop
def factorial(n):
    """
    Calculate the factorial of a number using a for loop.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of n.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial(5))  # Output: 120

#or

def factorial(n):
    result=1
    [result:=result*i for i in range(1,n+1)]
    return result

print(factorial(5))