### 12. Number Palindrome
def is_number_palindrome(num):
    """
    Check if a number is a palindrome.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is a palindrome, else False.
    
    Time Complexity: O(d), where d is the number of digits.
    Space Complexity: O(1)
    """
    str_num = str(num)
    return str_num == str_num[::-1]

#or

def reverse_number(num):
    reversed_num=0
    while  num>0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num=num//10
    return reversed_num

def num_palindrome(num):
    if num == reverse_number(num):
        return f"{num} is a palindrome number"
    else:
         return f"{num} is not a palindrome number"
     
print(num_palindrome(12321))