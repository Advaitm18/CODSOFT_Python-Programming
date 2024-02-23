import termtables as tt
from datetime import datetime, date
from termcolor import colored

tasks = []

def add_task(task,remark):
    tasks.append({"task":task, "completed":False, "remark":remark})
    print(colored("Task Added Successfully!!!","red"))
    
def list_tasks():
    print(colored(datetime.now().strftime('%B, %d %Y  %H:%M'),attrs=["bold"]))
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "✓"
        else:
            status = " "
        print(f"{index}. [{status}] {task['task']} {task['remark']}")
    print() 

def delete_task(choice):
    list_tasks()
    if len(tasks) == 0:
        print(colored("No Task To Delete ","red"))
    else:
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print(colored("Task Deleted Successfully.","red"))
        else:
            print("---> Invaild Task Number <---")

'''
def output(): 
   
    header = [colored("To-Do Tasks", attrs=["bold"])]
    
    data = [
        [list_tasks()]
    ]
    tt.print(data, header=header, padding=(0, 1), alignment="c")
'''

def mark_completed(index):
    if 1<= index <= len(tasks):
        tasks[index-1]["completed"] = True
        print(colored("Task marked as Complete!!!", "red"))
    else:
        print("---> Invaild Task Index <---")


while True:
    print("To-Do List Operations: ")
    print("\n1. Add The Task \n2. Delete The Task \n3. Update The Task Status \n4. View The Task Table \n5. Exit")
    option = int(input("---> "))
    print("-------------------------------------------------------------------------------------------------------------------------------")

    if option == 1:
        task = input("Enter the Task: ")
        print("Do you want to add remark to the Task (Y/N)?")
        opt = input("---> ").upper()
        if opt == "Y":
            remark = input(f"Enter the Remark for {task} task: ")
        elif opt == "N":
            remark = " "
        else:
            print("---> Invaild Input <---")
        add_task(task,remark)
        
    elif option == 2:
        choice = int(input("Enter the Task Number To Delete: "))
        delete_task(choice)
        
    elif option == 3:
        list_tasks()
        index = int(input("Enter the Task Number: "))
        mark_completed(index)
        
    elif option == 4:
        list_tasks()
        
    elif option == 5:
        break
        
    else:
        print("---> Invaild Option <---")
        
    
