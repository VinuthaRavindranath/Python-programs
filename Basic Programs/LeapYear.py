### 15. Leap Year
'''
A leap year is a year that contains an extra day, February 29, making it 366 days long 
instead of the usual 365 days. Leap years are necessary to keep our calendar in alignment with 
the Earth's orbit around the Sun, which takes approximately 365.25 days.

The rules for determining leap years using 4, 100, and 400 are based on the way the 
Gregorian calendar aligns with the Earth's orbit around the Sun.
'''


def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Parameters:
    year (int): The year to check.
    
    Returns:
    bool: True if it is a leap year, else False.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
print(is_leap_year(2020))  # Output: True

#or 
year=int(input("Please enter a year: "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print("its leap year")
else:
    print("its not a leap year")
    

#2000, 1996 and 1900