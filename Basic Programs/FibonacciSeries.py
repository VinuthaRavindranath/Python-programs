### 30. Fibonacci Series
'''
Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. 
Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers,
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
'''

list1=[0,1]
def fib(n):
    a,b,c=0,1,0
    for i in range(n+1):
        c=a+b
        list1.append(c)
        a=b
        b=c
    return list1

n= int(input("Enter a number: "))
print(fib(n))
    