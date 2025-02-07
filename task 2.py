A = float(input("Enter the first number ->"))
B = float(input("Enter the first number ->"))
operation = input("Enter the operation (*,/,-,+)")


if operation == "/":
    if B == 0:
        print("Erorr:Division by zero is not allowed!")
    else:
        result = A / B
        print("result =", result)
elif operation == "*":
    result = A * B 
    print("result =", result)
elif operation == "-":
    result = A-B
    print("result =", result)
elif operation == "+":
    result = A+B
    print("result =", result)
