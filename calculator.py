def addition(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def Multiplication(x,y):
    return(x*y)

def Division(x,y):
    return(x/y)

def main():
    x=int(input("Enter a first number: "))
    y=int(input("Enter a second number: "))
    z=(input("Enter the operand: "))
    result=0
    if(z=='+'):
        result+=addition(x,y)
    elif(z=='-'):
        result+=subtraction(x,y)
    elif(z=='*'):
        result+=Multiplication(x,y)
    elif(z=='/'):
        result+=Division(x,y)
    else:
        print("Please Enter a valid parameter.")
        return
    print(f"{x} {y} {z} = {result}")

if _name_ == "_main_":
    main()
