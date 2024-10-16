
## 46. Sort list of strings without using any inbuilt methods


# List of months to be sorted
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Bubble Sort Algorithm
n = len(months)  # Get the number of months
for i in range(n):  # Outer loop for each element
    for j in range(0, n-i-1):  # Inner loop for comparing adjacent elements
        # Compare adjacent elements
        if months[j] > months[j+1]:  
            # Swap if they are in the wrong order
            months[j], months[j+1] = months[j+1], months[j]

# Print the sorted list of months
print(months)
