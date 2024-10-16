### 16. Is Prime Number
def is_prime(n):
    """
    Check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, else False.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(13))  # Output: True

#or

def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def primeNums(startRange, endRange):
    list1=[]
    for i in range(startRange,endRange):
        if isPrime(i):
            list1.append(i)
    return list1
        
startRange=int(input("Enter the start range: "))
endRange=int(input("Enter the end range: "))
list2=primeNums(startRange,endRange)
print(list2)
