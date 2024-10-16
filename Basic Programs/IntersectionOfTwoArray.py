## 39. To Find the Intersection of Two Arrays

def intersection(arr1, arr2):
    """
    Find the intersection of two arrays.
    
    Parameters:
    arr1 (list): First array.
    arr2 (list): Second array.
    
    Returns:
    list: The intersection of the two arrays.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return list(set(arr1) & set(arr2))

# Example usage
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]


#or

def intersection(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))

print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
