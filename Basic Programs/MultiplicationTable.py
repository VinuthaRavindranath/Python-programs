### 17. Multiplication Table for a Given Number
def multiplication_table(n, limit=10):
    """
    Generate a multiplication table for a given number.
    
    Parameters:
    n (int): The number to create a table for.
    limit (int): The limit for the multiplication table (default is 10).
    
    Returns:
    list: A list containing the multiplication table.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return [n * i for i in range(1, limit + 1)]

# Example usage
print(multiplication_table(5))  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#or

def multiplicationTable(num):
    for i in range(1,11):
         print(f"{num} *{i} = {num*i}")
print(multiplicationTable(5))
    