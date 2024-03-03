from termcolor import colored              # !pip install termcolor
import termtables                         # !pip install termtables

print('''
      _____      _            _       _          
     / ____|    | |          | |     | |            
    | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |___| (_| | | (__| |_| | | (_| | || (_) | |   
     \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
\n''')

def add(x,y):                  # This function performs Addition 
    return x + y

def subtract(x,y):             # This function performs Subtraction 
    return x - y

def multiply(x,y):             # This function performs Multiplication 
    return x * y

def exponent(x,y):             # This function performs Exponentiation 
    return x ** y

def divide(x,y):               # This function performs Float Division
    return x / y

def floordivide(x,y):          # This function performs Floor Division
    return x // y

def tabledisplay(op,result):   # This function display the Operational Output
    my_table=[
        [f"{op}" , f"{result}"]
    ]
    headers= ["Arithmetic Operation","Operational Output"]
    termtables.print(my_table,header=headers,padding=(0,1),alignment="cc")
    
while True:
    print(colored("\nSelect The Arithmetic Operation: ", attrs=["bold"]))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exponentiation")
    print("5. Division (Float)")
    print("6. Division (Floor)")

    option = int(input("\n---> "))
    
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("\nEnter second number: "))
   
    if option == 1:
        op = f"{num1} + {num2}"
        result = f"{add(num1,num2)}"
        tabledisplay(op,result)
    elif option == 2:
        op = f"{num1} - {num2}"
        result = f"{subtract(num1,num2)}"
        tabledisplay(op,result)
    elif option == 3:
        op = f"{num1} * {num2}"
        result = f"{multiply(num1,num2)}"
        tabledisplay(op,result)
    elif option == 4:
        op = f"{num1} ** {num2}"
        result = f"{exponent(num1,num2)}"
        tabledisplay(op,result)
    elif option == 5:
        op = f"{num1} / {num2}"
        result = f"{divide(num1,num2)}"
        tabledisplay(op,result)
    elif option == 6:
        op = f"{num1} // {num2}"
        result = f"{floordivide(num1,num2)}"
        tabledisplay(op,result)
    else:
       print("Invalid input!! ")
          
    print("Do you want to continue y/n ??")
    choice= input("---> ").upper()
    if choice == "Y":
        continue
    elif choice == "N":
        break
    else:
        print("Invalid input!! ")
