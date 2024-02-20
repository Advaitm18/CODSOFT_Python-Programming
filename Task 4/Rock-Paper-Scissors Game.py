from random import choice         #In-Built Module:- Random.choice()
import Display                    #User-Defined Module
#from termcolor import colored  
#import termtable
print('''                              
         __      _____| | ___ ___  _ __ ___   ___ 
         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
          \ V  V /  __/ | (_| (_) | | | | | |  __/
           \_/\_/ \___|_|\___\___/|_| |_| |_|\___|                                         
''')
print("**************************************************************")

user_score = 0
comp_score = 0

while True:
    user_choice = input(" Enter:-     Rock(R)     Paper(P)     Scissors(S)     Exit(E) \n --->  ").upper()
    if user_choice == 'E':
        break
    elif user_choice == 'R':
        print("Rock")
        Display.display(user_choice)
    elif user_choice == 'P':
        print("Paper")
        Display.display(user_choice)
    elif user_choice == 'S':
        print("Scissors")
        Display.display(user_choice)
    else:
        print("Wrong input <---\n")
        continue
    
    option = ["R","P","S"]
    computer_choice = choice(option)
    print("Computer choose: ")
    #print(colored('Computer Choose: ','bold'))
    if computer_choice == 'R':
        print("Rock")
        Display.display(computer_choice)
    elif computer_choice == 'P':
        print("Paper")
        Display.display(computer_choice)
    else:
        computer_choice = 'S'
        print("Scissors")
        Display.display(computer_choice)

    if(user_choice == computer_choice):
        print("Draw")
    elif((user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R')):
        print("You won!")
        user_score += 1
    else:
        print("Computer won!")
        comp_score +=1

    print(f'''
    ---------------------------------
    | Your Score   | Computer Score |
    ---------------------------------
    |  {user_score}|  {comp_score}  |
    ---------------------------------
    ''')
    
    '''
    my_table=[
        [f"{user_score}" , f"{comp_score}"]
       ]
    headers= ["User_Score"," Computer_Score"]
    tt.print(my_table,header=headers,padding=(0,1),alignment="cc")
    '''
        
if(user_score>comp_score):
    print("\nYou have won!"+"\U0001F603")
elif(user_score<comp_score):
    print("\nYou have lost"+", Better Luck Next time! \U0001F605")
else:
    print("\nIt is a tie!"+"\U0001F611")

