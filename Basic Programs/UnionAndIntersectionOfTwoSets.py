## 23. To Find Union and Intersection of Two Sets
def union_and_intersection(set1, set2):
    """
    Find the union and intersection of two sets.
    
    Parameters:
    set1 (set): First set.
    set2 (set): Second set.
    
    Returns:
    tuple: (union, intersection)
    
    Time Complexity: O(n + m) where n and m are the sizes of the sets.
    Space Complexity: O(n + m)
    """
    
    union =set1.union(set2)
    intersection =set1.intersection(set2)
    # union = set1 | set2
    # intersection = set1 & set2
    return union, intersection



# Example usage
print(union_and_intersection({1, 2, 3}, {2, 3, 4}))  # Output: ({1, 2, 3, 4}, {2, 3}