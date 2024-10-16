### 14. Remove Duplicates from a List
def remove_duplicates(lst):
    # Remove duplicates while maintaining order
    return list(dict.fromkeys(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(lst))
# Time Complexity: O(n)
# Space Complexity: O(n)