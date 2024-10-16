### 12. Find the Intersection of Two Lists
def intersection(list1, list2):
    # Find common elements between two lists
    return list(filter(lambda x: x in list2, list1))

# Example usage
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print(intersection(list1, list2))
# Time Complexity: O(n*m)
# Space Complexity: O(n)