import string, random
from termcolor import colored     # !pip install termcolor

print('''
     _____                             _    _____                     _              
    |  _  |___ ___ ___ _ _ _ ___ ___ _| |  |   __|___ ___ ___ ___ ___| |_ ___ ___    
    |   __| .'|_ -|_ -| | | | . |  _| . |  |  |  | -_|   | -_|  _| .'|  _| . |  _|   
    |__|  |__,|___|___|_____|___|_| |___|  |_____|___|_|_|___|_| |__,|_| |___|_|    ''')
 
# Getting password length
length = int(input("\nSpecify the Password length: "))
characterList = ""
password = [] 

print("\nChoose character set for password : \n1. Digits \n2. Letters \n3. Special characters \n4. Exit")

while(True):
    choice = int(input("--->  ")) # Getting character set for the password
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Error! Enter a valid option.")

# This performs Password Generation 
for i in range(length):
    passchar = random.choice(characterList)   
    password.append(passchar)

print(colored(f"\nGENERATED PASSWORD: ", attrs=["bold"]),colored(f"{"".join(password)}", "red", attrs=["bold"]))
