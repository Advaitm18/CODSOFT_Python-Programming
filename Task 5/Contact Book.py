[0:32 pm, 10/03/2024] Advait_Mane: import re, os
from datetime import datetime    
from termcolor import colored              # !pip install termcolor

# Empty Contact list to Append entered data 
Contact = []

# This function is used to append entered details in the list(Contact)
def add_ContactDetail(name, phno, email, address):
    Contact.append({"Name": name, "Phone Number": phno, "Email-ID": email, "Address": address})
    print(colored("Contact Added Successfully !!!","green"))
    print(Contact)
    
# This function used to display the Contact-List
def list_contact():
    print(colored("CONTACT BOOK DETAILS","blue",attrs = ["bold"]))
    print(colored("\n" + datetime.now().strftime('%B, %d %Y  %H:%M'),attrs=["bold","blink"]))
    for index, contact in enumerate(Contact, start=1):
        print(f"\n{index}. {contact['Name']: <30} {contact['Phone Number']: <15} {contact['Email-ID']: <30} {contact['Address']}")
    print()

# This function is used to validate the entered Phone Number 
def isVaild_phno(phno):
    if re.match("^[6-9][0-9]{9}$", phno):
        print(colored("Valid Phone Number !", "green"))
    else:
        print(colored("Entered Phone No. is Invalid !", "red"))
        
# This function is used to validate the entered Email-ID
def isVaild_email(email):
    if re.match(r'^([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$', email):
        print(colored("Valid Email-Id !", "green"))
    else:
        print(colored("Entered Email-ID is Invalid !", "red"))

# This function used to delete the entered Contact Details
def delete_contact(choice):
    if not Contact:
        print(colored("No Contact To Delete. ","red"))
    else:
        if 0 < choice <= len(Contact):
            del Contact[choice-1]
            print(colored("Contact Deleted Successfully !!! ","green"))
        else:
            print("---> Invalid Contact Number <---")
            
def delete_all():
    return Contact.clear()
    
# This function used to search the Contact Details using Name
def search_contact(name):
    temp = []
    check = -1
    for i in range(len(Contact)):
        if name == Contact[i][1]:
            check = i
            temp.append(Contact[i])
  
# This function used to create .txt file of Contact Details
def create_contactbook():
    print(f"File Path: {os.getcwd()}")
    print(colored("File Created Successfully !!!", "green"))
    with open("Contact-Book.txt", "w") as file:
        file.write(datetime.now().strftime('%B, %d %Y  %H:%M'))
        for index, contact in enumerate(Contact, start=1):
            file.write(f"\n{index}. {contact['Name']: <25} {contact['Phone Number']: <15} {contact['Email-ID']: >30}  {contact['Address']}")
        file.write('\n')

while True:
    txt = "\nCONTACT BOOK Operations"
    print(colored(txt.center(50), attrs=["bold"]))
    print("\n1. Enter the Contact Details \n2. Delete the Contact \n3. Delete all the Contacts \n4. Search the Contact Details \n5. View Contact-Book \n6. Create Contact-Book File \n7. Exit")

    option = int(input("--->  "))
    print("-------------------------------------------------------------------------------------------------------------------------------")
    if option == 1:
        print("Enter Contact Details in the following order: ")
        name = input("Name: ")
        phno = input("Phone No. ")
        isVaild_phno(phno)
        email = input("Email-ID: ")
        isVaild_email(email)
        address = input("Current Address: ")

        add_ContactDetail(name, phno, email, address)
    
    elif option == 2:
        list_contact()
        choice = int(input("Enter the Contact Index Number To Delete: "))
        delete_contact(choice)

    elif option == 3:
        delete_all()
        
    elif option == 4:
        name = input("Please enter the category of the contact you wish to search: ")
        search_contact(name)
    
    elif option == 5:    
        list_contact()
        print("-------------------------------------------------------------------------------------------------------------------------------")

    elif option == 6:
        create_contactbook()
        
    elif option == 7:
        break

    else:
        print("---> Invalid Input <---")
[0:35 pm, 10/03/2024] Advait_Mane: import re, os
from datetime import datetime    
from termcolor import colored              # !pip install termcolor

# Empty Contact list to Append entered data 
Contact = []

# This function is used to append entered details in the list(Contact)
def add_ContactDetail(name, phno, email, address):
    Contact.append({"Name": name, "Phone Number": phno, "Email-ID": email, "Address": address})
    print(colored("Contact Added Successfully !!!","green"))
    print(Contact)
    
# This function used to display the Contact-List
def list_contact():
    print(colored("CONTACT BOOK DETAILS","blue",attrs = ["bold"]))
    print(colored("\n" + datetime.now().strftime('%B, %d %Y  %H:%M'),attrs=["bold","blink"]))
    for index, contact in enumerate(Contact, start=1):
        print(f"\n{index}. {contact['Name']: <30} {contact['Phone Number']: <15} {contact['Email-ID']: <30} {contact['Address']}")
    print()

# This function is used to validate the entered Phone Number 
def isVaild_phno(phno):
    if re.match("^[6-9][0-9]{9}$", phno):
        print(colored("Valid Phone Number !", "green"))
    else:
        print(colored("Entered Phone No. is Invalid !", "red"))
        
# This function is used to validate the entered Email-ID
def isVaild_email(email):
    if re.match(r'^([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$', email):
        print(colored("Valid Email-Id !", "green"))
    else:
        print(colored("Entered Email-ID is Invalid !", "red"))

# This function used to delete the entered Contact Details
def delete_contact(choice):
    if not Contact:
        print(colored("No Contact To Delete. ","red"))
    else:
        if 0 < choice <= len(Contact):
            del Contact[choice-1]
            print(colored("Contact Deleted Successfully !!! ","green"))
        else:
            print("---> Invalid Contact Number <---")
            
def delete_all():
    return Contact.clear()
    
# This function used to search the Contact Details using Name
def search_contact(name):
    temp = []
    check = -1
    for i in range(len(Contact)):
        if name == Contact[i][1]:
            check = i
            temp.append(Contact[i])
  
# This function used to create .txt file of Contact Details
def create_contactbook():
    print(f"File Path: {os.getcwd()}")
    print(colored("File Created Successfully !!!", "green"))
    with open("Contact-Book.txt", "w") as file:
        file.write(datetime.now().strftime('%B, %d %Y  %H:%M'))
        for index, contact in enumerate(Contact, start=1):
            file.write(f"\n{index}. {contact['Name']: <25} {contact['Phone Number']: <15} {contact['Email-ID']: >30}  {contact['Address']}")
        file.write('\n')

while True:
    txt = "\nCONTACT BOOK Operations"
    print(colored(txt.center(50), attrs=["bold"]))
    print("\n1. Enter the Contact Details \n2. Delete the Contact \n3. Delete all the Contacts \n4. Search the Contact Details \n5. View Contact-Book \n6. Create Contact-Book File \n7. Exit")

    option = int(input("--->  "))
    print("-------------------------------------------------------------------------------------------------------------------------------")
    if option == 1:
        print("Enter Contact Details in the following order: ")
        name = input("Name: ")
        phno = input("Phone No. ")
        isVaild_phno(phno)
        email = input("Email-ID: ")
        isVaild_email(email)
        address = input("Current Address: ")

        add_ContactDetail(name, phno, email, address)
    
    elif option == 2:
        list_contact()
        choice = int(input("Enter the Contact Index Number To Delete: "))
        delete_contact(choice)

    elif option == 3:
        delete_all()
        
    elif option == 4:
        name = input("Please enter the category of the contact you wish to search: ")
        search_contact(name)
    
    elif option == 5:    
        list_contact()
        print("-------------------------------------------------------------------------------------------------------------------------------")

    elif option == 6:
        create_contactbook()
        
    elif option == 7:
        print("Thank you for using Contact Book Application")
        break

    else:
        print("---> Invalid Input <---")
