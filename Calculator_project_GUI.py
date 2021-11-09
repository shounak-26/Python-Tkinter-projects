from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("350x400+300+300")
root.resizable(0,0)
root.title("calculator")
root.wm_iconbitmap("cal.ico")

val = ""

# *********  button Functions *******

def bt(number):
    global val
    val = val + str(number)
    data.set(val)

#************* Result ************

def Equal():
    global val
    try:
        result = eval(val)
        val = str(result)
        data.set(result)
    except:
        tmsg.showinfo("Notification","Something is wrong, try again")

#************* clear ************

def clear():
    global val
    val = ""
    data.set(val)

#************* Backspace ************

def back():
    global val
    b = len(lbl.get())
    lbl.delete(b-1,"end")
    if b == 1:
        lbl.insert(0,"0")
        val = ""
        data.set(val)


#Label
data = StringVar()

lbl = Entry(root,text = "Label",font="3ds 18 bold",justify = "right",textvariable = data,bg="white",fg="black",relief=SUNKEN)
lbl.pack(expand=True,fill=BOTH)

back = Button(lbl,text = "back",font="3ds 12 ",relief=GROOVE,bd=0,command=back,activebackground = "#ba68c8")
back.pack(anchor="s",side=LEFT)

#Frames

btrow1 = Frame(root)
btrow1.pack(expand = True,fill=BOTH)

btrow2 = Frame(root)
btrow2.pack(expand = True,fill=BOTH)

btrow3 = Frame(root)
btrow3.pack(expand = True,fill=BOTH)

btrow4 = Frame(root)
btrow4.pack(expand = True,fill=BOTH)


#BUTTONS

#Button 1
btn11 = Button(btrow1,text="1",padx= 10,pady=5,font="3ds 18 bold",relief=GROOVE,border=0,command=lambda:bt(1),bg="#e0e0e0",activebackground = "#ba68c8")
btn11.pack(side = LEFT,expand=True,fill = BOTH)

btn12 = Button(btrow1,text="2",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(2),bg="#e0e0e0",activebackground = "#ba68c8")
btn12.pack(side = LEFT,expand=True,fill = BOTH)

btn13 = Button(btrow1,text="3",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(3),bg="#e0e0e0",activebackground = "#ba68c8")
btn13.pack(side = LEFT,expand=True,fill = BOTH)

btn14 = Button(btrow1,text="+",font="3ds 18 bold",padx= 9,pady=5,relief=GROOVE,border=0,command=lambda:bt("+"),bg="#9e9e9e",activebackground = "#ba68c8")
btn14.pack(side = LEFT,expand=True,fill = BOTH)


#Button 2
btn21 = Button(btrow2,text="4",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(4),bg="#e0e0e0",activebackground = "#ba68c8")
btn21.pack(side = LEFT,expand=True,fill = BOTH)


btn22 = Button(btrow2,text="5",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(5),bg="#e0e0e0",activebackground = "#ba68c8")
btn22.pack(side = LEFT,expand=True,fill = BOTH)


btn23 = Button(btrow2,text="6",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(6),bg="#e0e0e0",activebackground = "#ba68c8")
btn23.pack(side = LEFT,expand=True,fill = BOTH)


btn24 = Button(btrow2,text="-",font="3ds 18 bold",padx= 12,pady=5,relief=GROOVE,border=0,command=lambda:bt("-"),bg="#9e9e9e",activebackground = "#ba68c8")
btn24.pack(side = LEFT,expand=True,fill = BOTH)


#Button 3
btn31 = Button(btrow3,text="7",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(7),bg="#e0e0e0",activebackground = "#ba68c8")
btn31.pack(side = LEFT,expand=True,fill = BOTH)

btn32 = Button(btrow3,text="8",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(8),bg="#e0e0e0",activebackground = "#ba68c8")
btn32.pack(side = LEFT,expand=True,fill = BOTH)

btn33 = Button(btrow3,text="9",font="3ds 18 bold",padx= 10,pady=5,relief=GROOVE,border=0,command=lambda:bt(9),bg="#e0e0e0",activebackground = "#ba68c8")
btn33.pack(side = LEFT,expand=True,fill = BOTH)

btn34 = Button(btrow3,text="*",font="3ds 18 bold",padx= 11,pady=5,relief=GROOVE,border=0,command=lambda:bt("*"),bg="#9e9e9e",activebackground = "#ba68c8")
btn34.pack(side = LEFT,expand=True,fill = BOTH)

#Button 4
btn41 = Button(btrow4,text="C",font="3ds 18 bold",padx= 22,pady=5,relief=GROOVE,border=0,command=clear,bg="#b71c1c",activebackground = "#ba68c8")
btn41.pack(side = LEFT,expand=True,fill = BOTH)

btn42 = Button(btrow4,text="0",font="3ds 18 bold",padx= 18,pady=5,relief=GROOVE,border=0,command=lambda:bt(0),bg="#e0e0e0",activebackground = "#ba68c8")
btn42.pack(side = LEFT,expand=True,fill = BOTH)

btn45 = Button(btrow4,text=".",font="3ds 25 bold",padx= 7,pady=2,relief=GROOVE,border=0,command=lambda:bt("."),bg="#9e9e9e",activebackground = "#ba68c8")
btn45.pack(side = LEFT,expand=True,fill = BOTH)

btn43 = Button(btrow4,text="=",font="3ds 18 bold",padx= 10,pady=2,relief=GROOVE,border=0,command=Equal,bg="#9e9e9e",activebackground = "#ba68c8")
btn43.pack(side = LEFT,expand=True,fill = BOTH)

btn44 = Button(btrow4,text="/",font="3ds 18 bold",padx= 10,pady=2,relief=GROOVE,border=0,command=lambda:bt("/"),bg="#9e9e9e",activebackground = "#ba68c8")
btn44.pack(side = LEFT,expand=True,fill = BOTH)


























root.mainloop()