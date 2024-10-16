## 22. Merge Two Lists and Sort Them

def merge_and_sort_lists(lst1, lst2):
    """
    Merge two lists and return a sorted list.
    
    Parameters:
    lst1 (list): First list.
    lst2 (list): Second list.
    
    Returns:
    list: The merged and sorted list.
    
    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) for the new list.
    """
    return sorted(lst1 + lst2)

# Example usage
print(merge_and_sort_lists([3, 1, 4], [2, 5, 0]))  # Output: [0, 1, 2, 3, 4, 5]


