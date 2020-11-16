#Simple Calculator App:
import tkinter as tk #Imports everything to do with Tkinter.
from math import* #Allows mathematic calculations to work.
'''
Very basic calculator able to do +,-,*,/ calculations.
Screen widget needs resolving to restrict clicking but not too much of an issue.
'''
root = tk.Tk() #Creates a Tk Window.

root.configure(bg="Orange") #Sets background color to orange.

#Add = sign:
def equals():
    resultScreen.insert(tk.END,'=') #Adds the '=' followinng the expression.
    calculation = resultScreen.get().split('=') #Splits on the '=', into a list allowing the first part to be evaluated.
    result = eval(calculation[0]) #'eval' the first element (the expression). Basically work out the result.
    resultScreen.insert(tk.END,result) #Following the '=', show the answer to the calculation. 
    
#Creates a label at top of page. .pack() organises widgets:
w = tk.Label(root, text="Calculator",bg="blue",fg="white").grid(row=0,column=2) 

#Creates the 'screen' box:
resultScreen = tk.Entry(root)
resultScreen.grid(row=1,column=2)
#resultScreen.configure(state='disabled') #Makes the screen read only.

#Creates the numbers as buttons:
one = tk.Button(text="1",command=lambda: resultScreen.insert(tk.END, "1") )
one.grid(row=2,column=1)
two = tk.Button(text="2",command=lambda: resultScreen.insert(tk.END, "2") )
two.grid(row=2,column=2)
three = tk.Button(text="3",command=lambda: resultScreen.insert(tk.END, "3") )
three.grid(row=2,column=3)
four = tk.Button(text="4",command=lambda: resultScreen.insert(tk.END, "4") )
four.grid(row=3,column=1)
five = tk.Button(text="5",command=lambda: resultScreen.insert(tk.END, "5") )
five.grid(row=3,column=2)
six = tk.Button(text="6",command=lambda: resultScreen.insert(tk.END, "6") )
six.grid(row=3,column=3)
seven = tk.Button(text="7",command=lambda: resultScreen.insert(tk.END, "7") )
seven.grid(row=4,column=1)
eight = tk.Button(text="8",command=lambda: resultScreen.insert(tk.END, "8") )
eight.grid(row=4,column=2)
nine = tk.Button(text="9",command=lambda: resultScreen.insert(tk.END, "9") )
nine.grid(row=4,column=3)
zero = tk.Button(text="0",command=lambda: resultScreen.insert(tk.END, "0") )
zero.grid(row=5,column=2)

#Equals and decimal point:
equals = tk.Button(text="=",command=equals)
equals.grid(row=5,column=1)
decimalPoint = tk.Button(text=".",command=lambda: resultScreen.insert(tk.END,"."))
decimalPoint.grid(row=5,column=3)

#Operation buttons:
divide = tk.Button(text="/",command=lambda: resultScreen.insert(tk.END,"/"))
divide.grid(row=2,column=4)
multiply = tk.Button(text="*",command=lambda: resultScreen.insert(tk.END,"*"))
multiply.grid(row=3,column=4)
minus = tk.Button(text="-",command=lambda: resultScreen.insert(tk.END,"-"))
minus.grid(row=4,column=4)
add = tk.Button(text="+",command=lambda: resultScreen.insert(tk.END,"+"))
add.grid(row=5,column=4)

#Clear button:
clear = tk.Button(text="CLEAR",bg="green",fg="white",command=lambda: resultScreen.delete(first=0,last=tk.END)).grid(row=6,column=2)

#Leave button:
leave = tk.Button(text="QUIT",bg="red",fg="white",command=lambda: root.destroy()).grid(row=6,column=3)

root.mainloop()
'''References
https://www.python-course.eu/tkinter_entry_widgets.php
https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
https://stackoverflow.com/questions/61492173/when-i-click-the-number-buttons-the-output-appears-to-the-left-of-the-previous#comment108777036_61492173
http://hplgit.github.io/primer.html/doc/pub/input/._input-readable003.html
'''
