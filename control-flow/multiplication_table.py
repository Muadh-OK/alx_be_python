number = int(input("Enter a number to see its multiplication table:"))

for i in range(1, 11): # Loop from 1 to 10
    result = number * i # calculate the product
    print (number, "*", i, "=", result)
