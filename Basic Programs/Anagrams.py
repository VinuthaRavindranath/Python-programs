### 33. Anagrams
def are_anagrams(s1, s2):
    """
    Check if two strings are anagrams.
    
    Parameters:
    s1 (str): First string.
    s2 (str): Second string.
    
    Returns:
    bool: True if they are anagrams, else False.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return sorted(s1) == sorted(s2)

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True