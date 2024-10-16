## 2. Write a Python program to sort a list of dictionaries using Lambda.

# Program to sort a list of dictionaries based on a specific key
dicts_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]

# Sort the list of dictionaries using a lambda function as the key
sorted_dicts = sorted(dicts_list, key=lambda x: x['age'])

# Output the sorted list
print(sorted_dicts)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Time Complexity: O(n log n), where n is the number of dictionaries
# Space Complexity: O(n) for storing the sorted list
