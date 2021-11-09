from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def myfunc():
    print(" Executed ")

def help():
    print("I will help you")
    tmsg.showinfo("Help","I can help you with this")

def rateus():
    print("Rate us")
    value = tmsg.askquestion("Was your experience is good?","You use this GUI...Was your experience is good?")
    if value == "yes":
        msg = "Rate us on appstore"
    else:
        msg = "Tell us what went wrong, we will contact you shortly !!!"
    tmsg.showinfo("Experience" , msg)

def open():
    ans = tmsg.askretrycancel("Ask", "Want to retry or cancel")
    if ans:
        print("You will retry this again")
    else:
        print(" cancelling for you")

root.geometry("544x344")
root.title("Menu and submenu")

mainmenu = Menu(root)

m1 = Menu(mainmenu , tearoff = 0)

m1.add_command(label = "New Project",command = myfunc)
m1.add_command(label = "Save",command = myfunc)
m1.add_command(label = "Save as",command = myfunc)
m1.add_separator()
m1.add_command(label = "Open",command = myfunc)
m1.add_command(label = "Delete",command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label= "File", menu=m1)

m2 = Menu(root,tearoff=0)

m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Cut",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Undo Copy",command=myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "Edit",menu = m2)

m3 = Menu(root,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rateus)
m3.add_command(label="Open",command=open)
mainmenu.add_cascade(label = "Help",menu = m3)
root.config(menu = mainmenu)

root.mainloop()