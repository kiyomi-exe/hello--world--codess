#Program: To make a simple calculator

num = int(input("Enter the numbers you want to perform operations on: "))
even = """Choose the operation you wish to perform by the integer associated with it:
        + = 1
        - = 2
        * = 3
        / = 4
        none of the above = 5
    """
odd = """Choose the operation you wish to perform by the integer associated with it:
        + = 1
        * = 2
        none of the above = 3
    """

if num==2:
    n1 = float(input("Enter your first greater number: "))
    n2 = float(input("Enter your second lower number: "))
    print(even)
    option = int(input("Choose the operation: "))
    if option==1:
        print("The addition of your numbers are: ",n1+n2)
    elif option==2:
        print("The difference of your numbers are: ",n1-n2)
    elif option==3:
        print("The multiplication of your numbers are: ",n1*n2)
    elif option==4:
        print("The division of your numbers are: ",n1/n2)
    else:
        print("More operations would be available soon. Thank you for your patience :)")

elif num==3:
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter your second number: "))
    n3 = float(input("Enter your third number: "))
    print(odd)
    option = int(input("Choose the operation: "))
    if option==1:
        print("The addition of your numbers are: ",n1+n2+n3)

    elif option==2:
        print("The multiplication of your numbers are: ",n1*n2*n3)

    else:
        print("More operations would be available soon. Thank you for your patience :)")

elif num==4:
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter your second number: "))
    n3 = float(input("Enter your third number: "))
    n3 = float(input("Enter your fourth number: "))
    print(odd)
    option = int(input("Choose the operation: "))
    if option==1:
        print("The addition of your numbers are: ",n1+n2+n3+n4)

    elif option==2:
        print("The multiplication of your numbers are: ",n1*n2*n3*n4)

    else:
        print("More operations would be available soon. Thank you for your patience :)")

elif num==5:
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter your second number: "))
    n3 = float(input("Enter your third number: "))
    n4 = float(input("Enter your fourth number: "))
    n5 = float(input("Enter your fifth number: "))
    print(odd)
    option = int(input("Choose the operation: "))
    if option==1:
        print("The addition of your numbers are: ",n1+n2+n3+n4+n5)

    elif option==2:
        print("The multiplication of your numbers are: ",n1*n2*n3*n4*n5)

    else:
        print("More operations would be available soon. Thank you for your patience :)")

else:
    print("More numbers to operate on will be available soon! ")
