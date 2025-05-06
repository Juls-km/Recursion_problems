def multiply (a, b):

    if b==0:
        return 0

    elif b<0:
        return -multiply(a,-b)

    else:
        return a+ multiply(a, b-1)

a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))

result=multiply(a,b)
print(f"The product of {a} and {b} is: {result}")

