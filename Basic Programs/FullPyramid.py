## 19. Full Pyramid

def full_pyramid(n):
    """
    Print a full pyramid of stars.
    
    Parameters:
    n (int): The number of rows.
    
    Time Complexity: O(n^2) due to nested loops.
    Space Complexity: O(1)
    """
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
full_pyramid(5)

#or


def fullPyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="  ")
        for k in range(2*i+1):
            print("*",end="  ")
        print()
        
fullPyramid(7)