### 9. Remove Leading and Trailing Whitespace
def strip_whitespace(strings):
    # Strip leading and trailing whitespace from strings
    return list(map(lambda s: s.strip(), strings))

# Example usage
strings = ["  hello  ", " world  "]
print(strip_whitespace(strings))
# Time Complexity: O(n)
# Space Complexity: O(n)
