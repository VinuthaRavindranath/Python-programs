## 11. String Palindrome

def string_palindrome(word):
    """
    Check if a string is a palindrome.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, else False.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if word==word[::-1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"
   
# Example usage 
print(string_palindrome("racecars")) #racecar is a palindrome