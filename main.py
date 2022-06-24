# AS91896 / AS91897


'''

Julie's Party Hire
This program will help keep track of which items are currently 
being hired with information such as the customer's full name,
receipt number, item name and quantity. The user can choose rows 
on the hire list to delete once items are returned.


'''


# Import Tkinter and Submodules
from itertools import count
from os import remove
from this import d
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from turtle import back, bgcolor
from unicodedata import name
from tkinter import messagebox


# Program settings
root = Tk()
root.title("Julie's Party Hire List") # title of our window
root.config(background="#202345") # 202345 is a hex colour code for a dark blue colour.
root.geometry("800x600") # size of our window
count = 0


# Define customized fonts
labelfont = Font(
    family="Avenir",
    size = 16,
    weight="bold")

entryfont = Font(
    family="Avenir",
    size = 12,
    weight="normal")

listfont = Font(
    family="Avenir",
    size = 13,
    weight="normal")

errorfont = Font(
    family="Avenir",
    size = 12,
    weight="bold")

headingfont = Font(
    family="Avenir",
    size = 13,
    weight="bold")

buttonfont = Font(
    family="Avenir",
    size = 13,
    weight="bold")


# Create a treeview widget
#  ↳ defining a style
style = ttk.Style()


#  ↳ selecting a theme for the treeview widget
style.theme_use("aqua")
style.configure("Treeview", 
    background="#f0f1fc",
    foreground="black",
    rowheight=25,
    fieldbackground="#f0f1fc",
    font=listfont
    )
style.configure("Treeview.Heading", font=headingfont)


style.map('Treeview',
    background=[('selected', '#5c66b5')])


# Define our Treeview widget
my_tree = ttk.Treeview(root)


#  ↳ define our column
my_tree['columns'] = ("Name", "Receipt", "Item", "Quantity")


#  ↳ formatte our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=CENTER, width=150)
my_tree.column("Receipt", anchor=CENTER, width=150)
my_tree.column("Item", anchor=CENTER, width=150)
my_tree.column("Quantity", anchor=CENTER, width=150)


#  ↳ create headings
my_tree.heading("#0", text=" ", anchor=CENTER)
my_tree.heading("Name", text="Full Name",anchor=CENTER)
my_tree.heading("Receipt", text="Receipt Number", anchor=CENTER)
my_tree.heading("Item", text="Item", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)

my_tree.pack(pady=20)


# Define a frame for displaying entry boxes
add_frame = Frame(root, bg="#202345") 
add_frame.pack()


# Create labels
nl = Label(add_frame, text="Full Name", font=labelfont, fg="White", bg="#202345") # nl = Name Label
nl.grid(row=0, column=0)

rl = Label(add_frame, text="Receipt Number", font=labelfont, fg="White", bg="#202345")
rl.grid(row=0, column=1)

il = Label(add_frame, text="Item", font=labelfont, fg="White", bg="#202345")
il.grid(row=0, column=2)

ql = Label(add_frame, text="Quantity", font=labelfont, fg="White", bg="#202345")
ql.grid(row=0, column=3)


# Create entry boxes
name_box = Entry(add_frame, font=entryfont)
name_box.grid(row=1, column=0)

receipt_box = Entry(add_frame, font=entryfont)
receipt_box.grid(row=1, column=1)

item_box = Entry(add_frame, font=entryfont)
item_box.grid(row=1, column=2)

quantity_box = Entry(add_frame, font=entryfont)
quantity_box.grid(row=1, column=3)


# Create error labels
name_box_error = Label(add_frame, font=errorfont, fg="Red", bg="#202345")
name_box_error.grid(row = 2, column=0)

receipt_box_error = Label(add_frame, font=errorfont, fg="Red", bg="#202345")
receipt_box_error.grid(row = 2, column=1)

item_box_error = Label(add_frame, font=errorfont, fg="Red", bg="#202345")
item_box_error.grid(row = 2, column=2)

quantity_box_error = Label(add_frame, font=errorfont, fg="Red", bg="#202345")
quantity_box_error.grid(row = 2, column=3)


# Function for checking the validity of each user input
def check_add_record_validity():
    #  ↳ clearing all error labels 
    clear_all_error_labels()
    
    #  ↳ define variable to check validity of fields
    allValid = True
    
    #  ↳ check if name is empty
    if name_box.get() == '':

        # Show error label to user
        name_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False

    # Setting a variable because we need to use it more than once. 
    receipt_box_input = receipt_box.get()

    #  ↳ check if receipt number is empty
    if receipt_box_input == '':
        
        # Show error label to user
        receipt_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False

    #  ↳ check if receipt number includes any alphabets
    elif not receipt_box_input.strip().isdigit():
        
        # Show error label to user
        receipt_box_error.config(text="Please only use numbers")

        # Set allValid to False
        allValid = False
    
    #  ↳ check if item is empty
    if item_box.get() == '':

        # Show error label to user
        item_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False
    
    # Setting a variable because we need to use it more than once. 
    quantity_box_input = quantity_box.get()

    #  ↳ check if quantity is empty
    if quantity_box_input == '':

        # Show error label to user
        quantity_box_error.config(text="This field is required")
        
        # Set allValid to False
        allValid = False

    #  ↳ check if receipt number includes any alphabets
    elif not quantity_box_input.strip().isdigit():
        
        # Show error label to user
        quantity_box_error.config(text="Please only use numbers")

        # Set allValid to False
        allValid = False

    # If all user inputs are valid, command Add Record
    if allValid == True:
        add_record()

    else:
        return


# Command to clear all labels before checking again. 
def clear_all_error_labels():
    name_box_error.config(text="")
    receipt_box_error.config(text="")
    item_box_error.config(text="")
    quantity_box_error.config(text="")


# Define command to add record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text=" ", 
        values=(name_box.get(), receipt_box.get(), item_box.get(), quantity_box.get()))
    count += 1

    #  ↳ clear boxes once data was displayed
    name_box.delete(0, END)
    receipt_box.delete(0, END)
    item_box.delete(0, END)
    quantity_box.delete(0, END)


# Define command to remove ALL records 
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# Define command to remove ALL selected
def remove_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


# Button to add records
add_record_button = Button(root, text="Add Record",
    font=buttonfont, command=check_add_record_validity) # commands to check validity when pressed
add_record_button.config(width=16)
add_record_button.pack(pady=20)


# Messagebox to pop up when the user presses "Remove ALL" button
def remove_all_confirm():
    if messagebox.askokcancel('WARNING', 'This cannot be undone. Are you sure?', icon="warning") == True:
        remove_all() # commands to remove ALL when pressed YES
    else:
        return  


# Button to remove all SELECTED.
remove_selected_button = Button(root, text="Remove all selected", font=buttonfont, command=remove_selected)
remove_selected_button.config(width=16)
remove_selected_button.pack()



# Button to remove ALL.
remove_all_button = Button(root, text="Remove all records",
    font=buttonfont, fg="Red", command=remove_all_confirm) # commands for the message box to pop up
remove_all_button.config(width=16)
remove_all_button.pack(pady=20)


# Run the program
root.mainloop()