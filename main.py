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
from tkinter import *
from tkinter import ttk
from tracemalloc import start


# Program settings
root = Tk()
root.title("Julie's Party Hire List")
root.geometry("800x600")


# Define customized fonts


# Start Page 


#  ↳ Define START 
def start():
    NONE
    # I left this command to do nothing for now. 

#  ↳ Create label to display name of the program

#  ↳ Define image for start button
start_image = PhotoImage(file="Resources/start2.png")

#  ↳ Create start button
start_button = Button(root, image=start_image, command=start, height=95, width=225)
start_button.pack(pady=220)
    # TODO: Place the start button lower on the screen without cutting off any of the image


# Create a ttk.Treeview widget 


#  ↳ Selecting a theme 

#  ↳ Create columns for the Treeview function

#  ↳ Format columns

#  ↳ Create headings


# Define a frame for displaying entry boxes


#  ↳ Create labels

#  ↳ Create entry boxes


# Append Button


#  ↳ Define append_details

#  ↳ Add append button


# Print Button


#  ↳ Define print_details

#  ↳ Add print button


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


