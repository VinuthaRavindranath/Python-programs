### 4. Calculate the Length of Each String in a List

def string_lengths(strings):
    # Return the lengths of each string in the list
    return list(map(lambda s: len(s), strings))

# Example usage
strings = ["hello", "world"]
print(string_lengths(strings)) #Output : [5, 5]