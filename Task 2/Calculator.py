print('''
      _____      _            _       _          
     / ____|    | |          | |     | |            
    | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |___| (_| | | (__| |_| | | (_| | || (_) | |   
     \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
    \n''')

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def exponent(x,y):
    return x ** y

def divide(x,y):
    return x / y

def floordivide(x,y):
    return x // y

while True:

    print("\nSelect Arithmetic Operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exponentiation")
    print("5. Division (Float)")
    print("6. Division (Floor)")
    print("7. Exit")

    option = int(input("\n---> "))
    
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("\nEnter second number: "))
    
    if option == 1:
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif option == 2:
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif option == 3:
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif option == 4:
        print(f"{num1} ** {num2} = {exponent(num1,num2)}")
    elif option == 5:
        print(f"{num1} / {num2} = {divide(num1,num2)}")   
    elif option == 6:
        print(f"{num1} // {num2} = {floordivide(num1,num2)}")
    elif option == 7:
        break
    else:
       print("Invalid input")
