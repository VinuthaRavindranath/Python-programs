### 34. String Compression
def string_compression(s):
    """
    Compress a string by counting consecutive characters.
    
    Parameters:
    s (str): The string to compress.
    
    Returns:
    str: The compressed string.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # for the last group
    return ''.join(compressed)

# Example usage
print(string_compression("aaabbc"))  # Output: "a3b2c1"