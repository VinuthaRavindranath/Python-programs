### 15. Count the Occurrences of Each Element
def count_occurrences(items):
    # Count occurrences of each element in a list
    return {item: items.count(item) for item in set(items)}

# Example usage
items = [1, 2, 2, 3, 3, 3]
print(count_occurrences(items))
# Time Complexity: O(n^2)
# Space Complexity: O(n)

#or

def count_occurances(items):
    dict1={}
    for item in items:
        dict1.update({item:items.count(item)})
    return dict1

items = [1,1, 2, 2, 3, 3, 3]
print(count_occurrences(items))