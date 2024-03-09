from random import choice         # In-Built Module:- Random.choice()
import Display                    # User-Defined Module 
import termtables as tt           # !pip install termtables
from termcolor import colored     # !pip install termcolor

print('''              _               
         __      _____| | ___ ___  _ __ ___   ___ 
         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
          \ V  V /  __/ | (_| (_) | | | | | |  __/
           \_/\_/ \___|_|\___\___/|_| |_| |_|\___|                                            
    ''')

user_score = 0
comp_score = 0


while True:
    # User Side operation
    user_choice = input("Choose any one Option:- Rock(R)    Paper(P)    Scissors(S)    Exit(E) \n --->  ").upper()  
    print("********************************************************************************")
    if user_choice == 'E':
        break
    elif user_choice == 'R':
        print(colored("User Choice: ", "red", attrs=["bold"]) + "Rock")
        Display.display(user_choice)
    elif user_choice == 'P':
        print(colored("User Choice: ", "red", attrs=["bold"]) + "Paper")
        Display.display(user_choice)
    elif user_choice == 'S':
        print(colored("User Choice: ", "red", attrs=["bold"]) + "Scissors")
        Display.display(user_choice)
    else:
        print("Wrong input <---\n")
        continue

    # Computer/bot side operation
    option = ["R","P","S"]
    computer_choice = choice(option)       # Random.choice() function 

    if computer_choice == 'R':
        print(colored("Computer Choice: ", "red", attrs=["bold"]) + "Rock")
        Display.display(computer_choice)
    elif computer_choice == 'P':
        print(colored("Computer Choice: ", "red", attrs=["bold"]) + "Paper")
        Display.display(computer_choice)
    else:
        computer_choice = 'S'
        print(colored("Computer Choice: ", "red", attrs=["bold"]) + "Scissors")
        Display.display(computer_choice)

    # Execution_result 
    if(user_choice == computer_choice):
        print(colored("Draw! ", "yellow", attrs=["bold"]))
    elif((user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R')):
        print(colored("You won! ", "yellow", attrs=["bold"]))
        user_score += 1
    else:
        print(colored("Computer won! ", "yellow", attrs=["bold"]))
        comp_score +=1

    # ScoreBoard_Display 
    my_table=[
        [f"{user_score}" , f"{comp_score}"]
       ]
    headers= ["User_Score"," Computer_Score"]
    tt.print(my_table,header=headers,padding=(0,1),alignment="cc")

# Final_Result      
if(user_score>comp_score):
    print(colored("\nYou have won!"+"\U0001F603", "green", attrs=["bold"] ))
elif(user_score<comp_score):
    print(colored("\nYou have lost, "+"Better Luck Next time! \U0001F605", "green", attrs=["bold"]))
else:
    print(colored("\nIt is a tie!"+"\U0001F611", "green", attrs=["bold"]))
