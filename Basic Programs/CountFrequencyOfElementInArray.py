### 45. To Count the Frequency of Elements in an Array
def count_frequency(arr):
    """
    Count the frequency of elements in an array.
    
    Parameters:
    arr (list): The array to process.
    
    Returns:
    dict: A dictionary with elements as keys and their frequencies as values.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

# Example usage
print(count_frequency([1, 2, 2, 3, 4, 4, 4]))  # Output: {1: 1, 2: 2, 3: 1, 4: 3}