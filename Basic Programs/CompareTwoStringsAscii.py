## 36. To Find if a=cat > b=dog (ASCII value)

def compare_strings(s1, s2):
    """
    Compare two strings based on ASCII value.
    
    Parameters:
    s1 (str): First string.
    s2 (str): Second string.
    
    Returns:
    bool: True if s1 > s2 based on ASCII, else False.
    
    Time Complexity: O(min(len(s1), len(s2)))
    Space Complexity: O(1)
    """
    return s1 > s2

# Example usage
print(compare_strings("cat", "dog"))  # Output: False

#Compare the first characters: 'c' (ASCII value 99) vs. 'd' (ASCII value 100).
#Since 99 < 100, "cat" is considered less than "dog".
