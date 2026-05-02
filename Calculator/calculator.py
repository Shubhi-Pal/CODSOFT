# Smart Calculator using match-case (Switch Style)

def calculator(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return "Cannot divide by zero" if b == 0 else a / b
        case _:
            return "Invalid operation"

# User input
print(" Simple Calculator ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Function calling
result = calculator(num1, num2, op)

print("Result:", result)