# Create a calculator using four functions:
# - add(a, b)
# - subtract(a, b)
# - multiply(a, b)
# - divide(a, b)
# Ask the user to enter two numbers and select an operation.

# Handle division by zero.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Invalid"
    return a/b

    
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))

print("1. Addition \n2. Subtraction \n3.Multiplication \n4.Division")

o = int(input("Enter an operator: "))

if o == 1:
     print("Addition of ",a," and ", b," is ", add(a,b) )

elif o == 2:
     print("Substraction of ",a," and ", b," is ", sub(a,b) )

elif o == 3:
     print("Multiplication of ",a," and ", b," is ", mul(a,b) )

elif o  == 4:
    print("Division of ",a," and ", b," is ", div(a,b) )

else:
    print("invalid choice")
