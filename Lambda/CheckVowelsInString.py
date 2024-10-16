### 10. Check for Vowels in a String
def contains_vowels(s):
    # Check if a string contains any vowels
    return any(map(lambda char: char in 'aeiou', s))

# Example usage
print(contains_vowels("hello"))
# Time Complexity: O(n)
# Space Complexity: O(1)