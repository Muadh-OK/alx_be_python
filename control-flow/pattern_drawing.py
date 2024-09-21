# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisks in the same line
    print()  # Move to the next line after one row is printed
    row += 1  # Move to the next row