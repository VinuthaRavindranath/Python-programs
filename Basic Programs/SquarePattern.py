## 30. Square Pattern
def square_pattern(n):
    """
    Print a square pattern of stars.
    
    Parameters:
    n (int): The number of rows and columns.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(n):
        print('*' * n)

# Example usage
square_pattern(4)

#or


def string_pattern(s,n):
    for i in range(n):
        for j in range(i+1):
            print(s*j)
        print()
        
print(string_pattern('abc',5))