program = True
while program:
    try:
        A = float(input("Enter the first number  or any letter To close ->"))
    except:
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
    