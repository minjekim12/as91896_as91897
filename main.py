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
    )

style.map("Treeview", 
    background=[('selected','#5c66b5')])

columns = ('#0', 'Name', 'Reciept', 'Item', 'Quantity')

# Define tree

tree = ttk.Treeview(root, columns=columns, show='headings')

# Create headings
tree.heading("#0", text=" ")
tree.heading("Name", text="Full Name")
tree.heading("Reciept", text="Reciept Number")
tree.heading("Item", text="Item")
tree.heading("Quantity", text="Quantity")

tree.pack(pady=20)

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

# Append Button



#  ↳ Define append_details


#  ↳ Add append button


# Print Button


#  ↳ Define print_details

def add_record():
    global count
    tree.insert(parent='', index='end', iid=count, text=" ", values=(name_box.get(), reciept_box.get(), item_box.get(), quantity_box.get()))
    count += 1

    # clear boxes
    name_box.delete(0, END)
    reciept_box.delete(0, END)
    item_box.delete(0, END)
    quantity_box.delete(0, END)
# remove all records



#  ↳ Add print button
print_button = Button(root, text="Add Record", command=add_record)
print_button.pack(pady=20)

# Remove selected rows button


#  ↳ Define remove_selected

#  ↳ Add remove selection button

#  ↳ Add messagebox to warn user


# Remove ALL rows button


#  ↳ Define remove_all

#  ↳ Add remove ALL button

#  ↳ Add messagebiox to warn user


# Quit Button


#  ↳ Define quit

#  ↳ Add quit button

#  ↳ Add messagebox to warn user


# Run the program
root.mainloop()


