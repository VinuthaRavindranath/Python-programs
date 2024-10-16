## 7. Extract First Character of Each String

def first_char(strings):
    # Extract the first character from each string
    return list(map(lambda s: s[0], strings))

# Example usage
strings = ["apple", "banana", "cherry"]
print(first_char(strings))
# Time Complexity: O(n)
# Space Complexity: O(n)

