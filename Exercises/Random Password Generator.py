#Random Password Generator
import random
from tkinter import *

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789' #All possible characters that could be included in output.

def generatePassword(): #Function to generate the password.
    password = "" #Initially the password is set to nothing.
    length = lengthInput.get()
    theLength = int(length)
    for i in range(theLength): #Loops as many times as the length.
        password += random.choice(characters) #After each loop it adds a random character to password.
    resultPassword.insert(END,password) #Inserts the result in the result box.
    return password

def clearBoxes():
    lengthInput.delete(first=0,last=END)
    resultPassword.delete(first=0,last=END)

def saveToTextFile():
    password = resultPassword.get() #Gets the password value so that it can be examined.
    while resultPassword.get() == "": #While the password hasn't been generated.
        pass #Do nothing.
    else:
        file = open("password.txt", "w") #Create a new textfile.
        file.write(password) #Write the generated value into that textfile.
        file.close() #Save and close the file.

root = Tk()

root.geometry("300x150") #Window dimensions.
root.configure(bg="orange") #Window color.

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open") #Opens a text file with a password stored in.
filemenu.add_command(label="Save",command=saveToTextFile) #Saves the result to a text file.
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit) #Closes the window.
menubar.add_cascade(label="File", menu=filemenu)

#Universal commands.
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
menubar.add_cascade(label="Edit")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

title = Label(root, text="Random Password Generator",bg="white") #Title at top  of window.
title.pack()

inputLabel = Label(root, text="Input the length of the password:") #Guides user to enter an integer.
inputLabel.pack()

lengthInput = Entry(root) #Where the user inputs the length.
lengthInput.pack()

outputLabel = Label(root, text="Output will be shown below:") #Guides user as to where result will be.
outputLabel.pack()

resultPassword = Entry(root) #Where the output will be shown.
resultPassword.pack()

generate = Button(root, text="Generate Password!",command=generatePassword) #Result is generated and displayed when this button is clicked.
generate.pack()

clearBoxes = Button(root, text="Clear",command=clearBoxes) #Clears values when pressed.
clearBoxes.pack()

root.mainloop()

'''
https://pythonspot.com/tk-menubar/#:~:text=Tkinter%20menubar&text=should%20have%20its%20own%20callback.&text=where%20root%20is%20a%20Tk,the%20menubar%20to%20attach%20to.
'''
