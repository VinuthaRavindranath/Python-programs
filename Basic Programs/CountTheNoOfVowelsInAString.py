## 10. Count the Number of Vowels in a Given String


def count_vowels(my_str):
    vowels="aeiouAEIOU"
    count=0
    for char in my_str:
        if char in vowels:
            count+=1
            
    return count

# Example usage
print(count_vowels("hello world"))  # Output: 3

#or

def count_vowels(s):
    """
    Count the number of vowels in a given string.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    int: The number of vowels in the string.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage
print(count_vowels("hello world"))  # Output: 3