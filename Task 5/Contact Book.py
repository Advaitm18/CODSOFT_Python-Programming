import re
from datetime import datetime

Contact = []

# To Add the entered data in Contact List
def add_ContactDetail(name, phno, email, address):
    Contact.append({"Name":name, "Phone Number":phno, "Email-ID":email, "Address":address})
    print("Contact Added Successfully!!!")
    print(Contact)

# To Display the data in "Contact_Book.txt" file  
def list_contact():
    print(datetime.now().strftime('%B, %d %Y  %H:%M'))
    for index, contact in enumerate(Contact, start=1):
        print(f"{index}. {contact['contact']} {contact['phno']} {contact['email']} \n{contact['address']}")
    print() 

            
# To valided the entered Phone Number
def isVaild_phno(phno):     
    pattern = re.compile("[6-9][0-9]{9}")
    if re.fullmatch(pattern, phno):
        print("Vaild Phone Number !!")
    else:
        print("Entered Phone No. is Invalid!! ")
        
# To valided the entered Emai-ID
def isVaild_email(email):
    pattern = re.compile('([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(pattern, email):
        print("Vaild Email-Id !!")
    else:
        print(colored("Entered Email-ID is Invaild!! ","red"))

# To Delete Contact (Option (2))
def delete_contact(choice):
    list_contact()
    if len(Contact) == 0:
        print("No Contact To Delete ")
    else:
        if 0 < choice <= len(Contact):
            del Contact[choice-1]
            print("Task Deleted Successfully.")
        else:
            print("---> Invaild Contact Number <---")
            
# To View Contact_Book (Option (3))
def view_contact():
    file = open("Contact_Book.txt")
    content = file.read()
    print(content)
    file.close()

while True:
    print(("CONTACT BOOK").center(50))
    print("1. Enter the Contact Details 2.Delete the Contact 3.View Contact-Book 4.Exit")

    option = int(input("--->  "))
    if option == 1:
        name = input("Enter the Name: ")
        phno = input("Enter the Mobile Number: ")
        isVaild_phno(phno)
        email = input("Enter the Email-ID: ")
        isVaild_email(email)
        address = input("Enter the Address: ")

        add_ContactDetail(name, phno, email, address)
        
        #display = f"{('{: <25}'.format(name))} {('{: <15}'.format(phno))} {email} \n{address}"
        file = open("Contact_Book.txt","a")
        file.write(list_contact())
        file.close()
        
    elif option == 2:
        choice = int(input("Enter the Contact Index Number To Delete: "))
        delete_contact(choice)
        
    elif option == 3:
        view_contact(choice)
        
    elif option == 4:
        break
    else:
        print("---> Invaild Input <---")


