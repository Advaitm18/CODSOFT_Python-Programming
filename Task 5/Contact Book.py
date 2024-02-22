# importing the required modules  
import tkinter as tk                    # importing the tkinter module as tk  
from tkinter import ttk                 # importing the ttk module from the tkinter library  
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql                   # importing the sqlite3 module as sql  
  
 
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:   
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()   
        task_field.delete(0, 'end')  
  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)  
  
def update_task():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:   
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
    
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:  
            tasks.remove(the_value)   
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:    
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
   
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:   
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  

def clear_list():  
    task_listbox.delete(0, 'end')  

def view_task():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:   
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  

def close():  
    print(tasks) 
    guiWindow.destroy()

# defining another label using the ttk.Label() widget  
def task_label(text_name,placex,placey):
    task_label = ttk.Label(  
        functions_frame,  
        text = text_name,  
        font = ("Times New Roman", "14", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )  
    task_label.place(x = placex, y = placey)
    
def task_field(placex,placey):  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = placex, y = placey)  
  
# function to retrieve data from the database  
def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from tasks'):  
        # using the append() method to insert the titles from the table in the list  
        tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
    guiWindow = tk.Tk()   
    guiWindow.title("Contact Book")  
    guiWindow.geometry("700x550+350+50")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#F0F8FF")  
  
    # using the connect() method to connect to the database  
    the_connection = sql.connect('listOfTasks.db')  
    # creating the cursor object of the cursor class  
    the_cursor = the_connection.cursor()  
    # using the execute() method to execute a SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    # defining an empty list  
    tasks = []  
      
    # defining frames using the tk.Frame() widget  
    header_frame = tk.Frame(guiWindow, bg = "#87CEFA")  
    functions_frame = tk.Frame(guiWindow, bg = "#87CEFA")  
    listbox_frame = tk.Frame(guiWindow, bg = "#87CEFA")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "Contact Book",  
        font = ("Impact", "40"),  
        background = "#87CEFA",  
        foreground = "#002D72"  
    )  
    header_label.pack(padx = 20, pady = 20)

    task_label("Name: ",30,10)
    task_label("Phone Number: ",30,50)
    task_label("Email-ID: ",30,90)
    task_label("Address: ",30,130)

    task_field(160,10)
    task_field(160,50)
    task_field(160,90)
    task_field(160,130)
  
    # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Contact",  
        width = 20,  
        command = add_task  
    )

    update_button = ttk.Button(
        functions_frame,
        text = "Update Contact",
        width = 20,
        command = update_task
    )
    
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Contact",  
        width = 20,  
        command = delete_task  
    )
    
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Contacts",  
        width = 20,  
        command = delete_all_tasks  
    )
    
    view_button = ttk.Button(
        functions_frame,
        text = "View Contact",
        width = 20,
        command = view_task
    )
    
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 20,  
        command = close  
    )
    
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 200)
    update_button.place(x = 30, y = 240)
    del_button.place(x = 30, y = 280)  
    del_all_button.place(x = 30, y = 320)
    view_button.place(x = 30, y = 360)
    exit_button.place(x = 30, y = 400)  
   
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 35,  
        height = 20,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#0071c5",  
        selectforeground = "#FFFFFF"  
    )  
    task_listbox.place(x = 15, y = 20)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  




