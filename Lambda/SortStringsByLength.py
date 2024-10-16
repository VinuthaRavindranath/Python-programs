
### 12. Sort Strings by Length
def sort_by_length(strings):
    # Sort strings based on their lengths
    return sorted(strings, key=lambda s: len(s))

# Example usage
strings = ["verylong" ,"short", "medium"]
print(sort_by_length(strings))
# Time Complexity: O(n log n)
# Space Complexity: O(n)