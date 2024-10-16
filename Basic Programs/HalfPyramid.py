### 18. Half Pyramid
def half_pyramid(n):
    """
    Print a half pyramid of stars.
    
    Parameters:
    n (int): The number of rows.
    
    Time Complexity: O(n^2) due to nested loops.
    Space Complexity: O(1)
    """
    for i in range(1, n + 1):
        print('* ' * i)

# Example usage
half_pyramid(5)

#or
def halfpyramid(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=" ")
        print()

n=int(input("enter a number: "))
halfpyramid(n)