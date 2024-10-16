## 31. String Pattern
def string_pattern(s, n):
    """
    Print a pattern of a string.
    
    Parameters:
    s (str): The string to print.
    n (int): The number of times to repeat the string.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, n + 1):
        print(s * i)

# Example usage
string_pattern('abc', 3)