## Using list comprehension convert given list with square of even numbers.Given_list = [1,4,3,6,8] result = [1,16,3,36,64]

def square_even_numbers(given_list):
    """
    Replace even numbers in the given list with their squares.

    Parameters:
    given_list (list): A list of integers.

    Returns:
    list: A new list with even numbers replaced by their squares.

    Time Complexity:
    O(n), where n is the number of elements in the given_list.

    Space Complexity:
    O(n), for the new list created to store the results.
    """
    return [i*i if i %2 ==0 else i for i in given_list ]

# Example usage
Given_list = [1, 4, 3, 6, 8]
result = square_even_numbers(Given_list)
print(result)
