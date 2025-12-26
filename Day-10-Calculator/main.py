import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1/n2


n1 = float(input("Enter the first number: "))
operation = input("For Addition +\nFor Subtraction -\nFor Multiplication *\nFor Division /\n")
n2 = float(input("Enter the second number: "))
if operation == "+":
    print(add(n1, n2))
    n1 = n1 + n2
elif operation == "-":
    print(subtract(n1, n2))
    n1 = n1 - n2
elif operation == "*":
    print(multiply(n1, n2))
    n1 = n1 * n2
else:
    print(divide(n1, n2))
    n1 = n1 / n2


while True:
    cont = input("Want to continue? yes or no ").lower()
    if cont == "yes":
        operation = input("For Addition +\nFor Subtraction -\nFor Multiplication *\nFor Division /\n")
        n2 = float(input("Enter the second number: "))
        if operation == "+":
            print(add(n1, n2))
            n1 = n1 + n2
        elif operation == "-":
            print(subtract(n1, n2))
            n1 = n1 - n2
        elif operation == "*":
            print(multiply(n1, n2))
            n1 = n1 * n2
        elif operation == "/":
            result = divide(n1, n2)
            print(result)
            if isinstance(result, str):  #This insinstance function was a sonnet 4.5 addition to better
                continue                 #the code functionality for the user.
            n1 = result                  #Pls note that rest everything is written by me.
    else:
        print(f"Final answer is\n {n1}")
        break
