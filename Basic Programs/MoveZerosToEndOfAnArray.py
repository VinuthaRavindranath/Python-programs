### 42. Move Zeros to the End of the Array
def move_zeros(arr):
    """Move all zeros in the array to the end."""
    non_zero = [num for num in arr if num != 0]
    zero_count = arr.count(0)
    return non_zero + [0] * zero_count

# Example usage
arr = [0, 1, 0, 3, 12]
print(move_zeros(arr))  # Output: [1, 3, 12, 0, 0]
# Time Complexity: O(n)
# Space Complexity: O(n)
