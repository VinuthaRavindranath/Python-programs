## 3. Filter Even Numbers from a List

def filter_even_numbers(nums):
    # Filter out even numbers from the list
    return list(filter(lambda x: x % 2 == 0, nums))

# Example usage
nums = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(nums))
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Python’s filter() is a built-in function that allows you to process an iterable and 
extract those items that satisfy a given condition. This process is commonly known as a filtering operation. 
With filter(), you can apply a filtering function to an iterable and produce a new iterable with the items that satisfy the condition at hand. 
In Python, filter() is one of the tools you can use for functional programming.

https://realpython.com/python-filter-function/
'''