def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Simple Claculator:")
x=int(input("Enter your First number: "))
y=int(input("Enter your Second number: "))
print("Select option: ")
print("A for Addition.")
print("S for subtraction.")
print("M for Multiplication.")
print("D for Division.")
print("E for Exit.")
while(True):
    opt=input("Enter the options from (A/S/M/D/E): ")
    if opt in ('A','S','M','D','E'):
        if opt == 'A':
            print("Addition of two numbers",x,"and",y,"is:",add(x,y))
        elif opt == 'S':
            print("Subtraction of two numbers",x,"and",y,"is:",sub(x,y))
        elif opt == 'M':
            print("Multiplication of two numbers",x,"and",y,"is:",mul(x,y))
        elif opt == 'D':
            print("Division of two numbers",x,"and",y,"is: ",div(x,y))
        elif opt == 'E':
            print("Thank you")
            exit()
    else:
        print("Wrong Choice.")
