# AS91896 / AS91897


'''

Julie's Party Hire
This program will help keep track of which items are currently 
being hired with information such as the customer's full name,
reciept number, item name and quantity. The user can choose rows 
on the hire list to delete once items are returned.

The program also allows a group to delete their row by choosing which row
to delete if they are moving on.

'''


# Import Tkinter and Submodules
from itertools import count
from os import remove
from this import d
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from turtle import bgcolor
from unicodedata import name
from tkinter import messagebox


# Program settings
root = Tk()
root.title("Julie's Party Hire List")
root.geometry("800x600")
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
#  ↳ Selecting a theme 
style = ttk.Style()

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


# Define tree

my_tree = ttk.Treeview(root)

#define our column
my_tree['columns'] = ("Name", "Reciept", "Item", "Quantity")

# formatte our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=CENTER, width=150)
my_tree.column("Reciept", anchor=CENTER, width=150)
my_tree.column("Item", anchor=CENTER, width=150)
my_tree.column("Quantity", anchor=CENTER, width=150)

# Create headings
my_tree.heading("#0", text=" ", anchor=CENTER)
my_tree.heading("Name", text="Full Name",anchor=CENTER)
my_tree.heading("Reciept", text="Reciept Number", anchor=CENTER)
my_tree.heading("Item", text="Item", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)

my_tree.pack(pady=20)

# Define a frame for displaying entry boxes
add_frame = Frame(root)
add_frame.pack()

#  ↳ Create labels
nl = Label(add_frame, text="Full Name", font="Helvetica") # nl = Name Label
nl.grid(row=0, column=0)

rl = Label(add_frame, text="Reciept Number", font="Helvetica")
rl.grid(row=0, column=1)

il = Label(add_frame, text="Item", font="Helvetica")
il.grid(row=0, column=2)

ql = Label(add_frame, text="Quantity", font="Helvetica")
ql.grid(row=0, column=3)

#  ↳ Create entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)
reciept_box = Entry(add_frame)
reciept_box.grid(row=1, column=1)
item_box = Entry(add_frame)
item_box.grid(row=1, column=2)
quantity_box = Entry(add_frame)
quantity_box.grid(row=1, column=3)

# Create error labels
name_box_error = Label(add_frame)
name_box_error.grid(row = 2, column=0)
reciept_box_error = Label(add_frame)
reciept_box_error.grid(row = 2, column=1)
item_box_error = Label(add_frame)
item_box_error.grid(row = 2, column=2)
quantity_box_error = Label(add_frame)
quantity_box_error.grid(row = 2, column=3)

def check_add_record_validity():
    clear_all_error_labels()
    
    # define variable to check validity of fields
    allValid = True
    
    # check if name is empty

    
    if name_box.get() == '':
        # make name entry field red
        name_box_error.config(text="This field is required")

        # set allValid to False
        allValid = False

    reciept_box_input = reciept_box.get()
    if reciept_box_input == '':

        reciept_box_error.config(text="This field is required")

        allValid = False
    elif not reciept_box_input.strip().isdigit():

        reciept_box_error.config(text="Please only use numbers")
        allValid = False
    
    if item_box.get() == '':

        item_box_error.config(text="This field is required")
        allValid = False
    quantity_box_input = quantity_box.get()
    if quantity_box_input == '':

        quantity_box_error.config(text="This field is required")

        allValid = False
    elif not quantity_box_input.strip().isdigit():

        quantity_box_error.config(text="Please only use numbers")
        allValid = False

    if allValid == True:
        add_record()
    else:
        return


def clear_all_error_labels():
    name_box_error.config(text="")
    reciept_box_error.config(text="")
    item_box_error.config(text="")
    quantity_box_error.config(text="")






#  ↳ Define add_record

def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text=" ", values=(name_box.get(), reciept_box.get(), item_box.get(), quantity_box.get()))
    count += 1

    # clear boxes
    name_box.delete(0, END)
    reciept_box.delete(0, END)
    item_box.delete(0, END)
    quantity_box.delete(0, END)



def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

#remove all rows selected
def remove_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


#  ↳ Add print button
add_record_button = Button(root, text="Add Record", font=buttonfont, command=check_add_record_validity)
add_record_button.config(width=16)
add_record_button.pack(pady=20)


#define remove all confirmation message box
def remove_all_confirm():
    if messagebox.askokcancel('WARNING', 'This cannot be undone. Are you sure?', icon="warning") == True:
        remove_all()
    else:
        return  


# remove one
remove_selected_button = Button(root, text="Remove all selected", font=buttonfont, command=remove_selected)
remove_selected_button.config(width=16)
remove_selected_button.pack()



# remove all
remove_all_button = Button(root, text="Remove all records", font=buttonfont, fg="Red", command=remove_all_confirm)
remove_all_button.config(width=16)
remove_all_button.pack(pady=20)




# Quit Button


#  ↳ Define quit

#  ↳ Add quit button

#  ↳ Add messagebox to warn user


# Run the program
root.mainloop()


