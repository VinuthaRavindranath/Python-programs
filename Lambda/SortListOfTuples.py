## 1. Write a python program to sort a list of tuples using Lambda.

# Program to sort a list of tuples based on the second element
tuples_list = [(1, 3), (4, 1), (2, 2), (3, 4)]

# Sort the list of tuples using a lambda function as the key
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])

# Output the sorted list
print(sorted_tuples)  # Output: [(4, 1), (2, 2), (1, 3), (3, 4)]

# Time Complexity: O(n log n), where n is the number of tuples
# Space Complexity: O(n) for storing the sorted list
