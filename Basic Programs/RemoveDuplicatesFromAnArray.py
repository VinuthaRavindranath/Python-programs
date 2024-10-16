## 40. To Remove Duplicates from an Array

def remove_duplicates(arr):
    """
    Remove duplicates from an array.
    
    Parameters:
    arr (list): The array to process.
    
    Returns:
    list: The array without duplicates.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return list(set(arr))

# Example usage
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]

#or
def remove_duplicates(arr):
    arr2=[]
    for i in arr:
        if i not in arr2:
            arr2.append(i)
    return arr2

print(remove_duplicates([1, 2, 2, 3, 4, 4]))