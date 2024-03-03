import re, os
from datetime import datetime    
from termcolor import colored              # !pip install termcolor

# Empty Contact list to Append entered data 
Contact = []

# This function is used to append entered details in the list(Contact)
def add_ContactDetail(name, phno, email, address):
    Contact.append({"Name": name, "Phone Number": phno, "Email-ID": email, "Address": address})
    print(colored("Contact Added Successfully !!!","green"))

# This function used to display the Contact-List
def list_contact():
    print(colored("CONTACT BOOK","blue",attrs = ["bold"]))
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
    txt = "\nCONTACT BOOK"
    print(colored(txt.center(50), attrs=["bold"]))
    print("\n1. Enter the Contact Details \n2. Delete the Contact \n3. View Contact-Book \n4. Create Contact-Book File \n5. Exit")

    option = int(input("--->  "))
    print("-------------------------------------------------------------------------------------------------------------------------------")
    if option == 1:
        name = input("Enter the Name: ")
        phno = input("Enter the Contact No. ")
        isVaild_phno(phno)
        email = input("Enter the Email-ID: ")
        isVaild_email(email)
        address = input("Enter the Address: ")

        add_ContactDetail(name, phno, email, address)
    
    elif option == 2:
        list_contact()
        choice = int(input("Enter the Contact Index Number To Delete: "))
        delete_contact(choice)
    
    elif option == 3:    
        list_contact()
        print("-------------------------------------------------------------------------------------------------------------------------------")

    elif option == 4:
        create_contactbook()
        
    elif option == 5:
        break

    else:
        print("---> Invalid Input <---")
