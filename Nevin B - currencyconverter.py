#Making a list of Currencies
import tkinter

currency_type = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Nevin - Currency Conversion")
 ##Dimensions of the Converter

#Defining my variables
variable1 = StringVar(root)
variable2 = StringVar(root)

#Pop up Title
headlabel = Label(font=("Helvetica", 20), text = '  Pypower Project   :    Currency Converter  ', bg= '#663300',fg='white')
headlabel.grid(row=1, column=0,sticky=W)

#Currency exchange code
def realtimecurrencyconversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_cur = variable1.get()
    to_cur = variable2.get()

    if amount1_field.get() == "":
        messagebox.showerror("ERROR!", "Please enter an amount")

    elif from_cur=="Currency" or to_cur =="Currency":
        messagebox.showerror("ERROR!", "Please selet your currencies")

    else:
        new_amt = c.convert(from_cur, to_cur, float(amount1_field.get()))
        amount2_field.insert(INSERT, str(new_amt))

def clearall():
    amount1_field.delete(0, tkinter.END)
    amount2_field.delete(0, tkinter.END)

#Setting up my labels

Label_1 = Label(root, font=("Helvetica", 20), text="",padx=2,pady=2, bg="White",fg ="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = Label(root,font=("Helvetica, 20"), text = "\tAmount:  ", bg="White",fg = "Black")
label1.grid(row=2, column=0, sticky=W)

label1 = Label(root,font=("Helvetica", 20), text = "\tFrom Currency:  ", bg="White",fg = "black")
label1.grid(row=3, column=0, sticky=W)

label1 = Label(root,font=("Helvetica", 20), text = "\tTo Currency:  ", bg="White",fg = "black")
label1.grid(row=4, column=0, sticky=W)

label1 = Label(root,font=("Helvetica", 20), text = "\tConverted Amount:  ", bg="White",fg = "black")
label1.grid(row=8, column=0, sticky=W)

Label_1 =Label(root, font=("Helvetica", 20), text="",padx=2,pady=2, bg="White",fg ="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 =Label(root, font=("Helvetica", 20), text="",padx=2,pady=2, bg="White",fg ="black")
Label_1.grid(row=7, column=0, sticky=W)

Label_9 =Button(root, font=('arial', 15,'bold'), text="   Convert  ",padx=2,pady=2, bg="blue",fg = "white",command=realtimecurrencyconversion)
Label_9.grid(row=6, column=0)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=9, column=0,sticky=W)

Label_9 =Button(root, font=("Helvetica", 20), text=" Clear All  ",padx=2,pady=2, bg="white",fg = "red",command=clearall)
Label_9.grid(row=10, column=0)

#Setting up my currency to currency buttons
from_cur = OptionMenu(root, variable1, *currency_type)
to_cur = OptionMenu(root, variable2, *currency_type)

from_cur.grid(row = 3, column = 0, ipadx = 45,sticky=E)
to_cur.grid(row = 4, column = 0, ipadx = 45,sticky=E)

#Setting up my amount fields
amount1_field = Entry(root)
amount1_field.grid(row=2,column=0,ipadx =20,sticky=E)

amount2_field = Entry(root)
amount2_field.grid(row=8,column=0,ipadx =31,sticky=E)


root.mainloop()