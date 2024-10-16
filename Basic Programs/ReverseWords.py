### 7. Reverse the Order of the Words
def reverse_words(s):
    """
    Reverse the order of words in a given string.
    
    Parameters:
    s (str): The string to reverse words in.
    
    Returns:
    str: The string with words in reverse order.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the list of words.
    """
    return ' '.join(s.split()[::-1])

# Example usage
print(reverse_words("hello world"))  # Output: "world hello"