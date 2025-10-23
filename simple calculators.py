print("Simple Calculator")
print("Choose an operation: +, -, *, /")

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
        result = num1 / num2
else:
    result = "nonsense!"

# Print the result
print("Result:", result)
