### 25. To Merge Two Dictionaries
def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries into one.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary.
    
    Time Complexity: O(n + m), where n and m are sizes of the dictionaries.
    Space Complexity: O(n + m)
    """
    merged ={**dict1,**dict2} 
    return merged

# Example usage
print(merge_dictionaries({'a': 1}, {'b': 2}))  # Output: {'a': 1, 'b': 2}

