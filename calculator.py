def calculator(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    if num2 == 0:
      raise ZeroDivisionError("Error: Cannot divide by zero")
    return num1 / num2
  else:
    raise ValueError("Invalid operation. Please use +, -, *, or /.")

# Get user input
while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, or /): ")
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

# Perform the calculation and handle errors
try:
  result = calculator(num1, num2, operation)
  print(f"The result of {num1} {operation} {num2} is: {result}")
except (ValueError, ZeroDivisionError) as e:
  print(e)
