### 44. Prove that String is Immutable
def prove_string_immutable():
    """
    Demonstrate that strings are immutable in Python.
    """
    s = "hello"
    try:
        s[0] = 'H'  # Attempt to modify the first character
    except TypeError as e:
        return str(e)  # Capture the exception

# Example usage
print(prove_string_immutable())  # Output: 'str' object does not support item assignment