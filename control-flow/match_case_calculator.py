num1 = int(input("Enter the first number: "))
num2 = int(input("ENter the second number: "))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = num1 / num2
    case _:
        result = "Invalid Operation."

print("The rsult is:", result)