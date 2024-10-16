## 24. To Check if the Set is a Subset
def is_subset(set1, set2):
    """
    Check if set1 is a subset of set2.
    
    Parameters:
    set1 (set): The potential subset.
    set2 (set): The superset.
    
    Returns:
    bool: True if set1 is a subset of set2, else False.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return set1.issubset(set2)

# Example usage
print(is_subset({1, 2}, {1, 2, 3}))  # Output: True