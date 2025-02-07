program = True
while program:
    A = str(input("Enter the first number  or To close Enter L ->"))
    if A == "L":
        print("program closed")
        program= False
        break
    
    B = float(input("Enter the second number ->"))
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
    