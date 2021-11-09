#------------------------- Buttons Functions -----------------------

def addstudent():
    addroot = Toplevel(master=Dataentryframe)
    addroot.geometry('500x490+20+180')
    addroot.grab_set()
    addroot.title("Add student")
    addroot.iconbitmap('sql_c.ico')
    addroot.resizable(False, False)
    addroot.config(bg='#616161')

    def addstudent():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")

        if(len(name)==0):
            messagebox.showerror('Error','name should not be empty')
        elif(len(email)==0):
            messagebox.showerror('Error', 'E-mail should not be empty')
        elif (len(mobile) == 0):
            messagebox.showerror('Error', 'Mobile should not be empty')
        else:
            try:
                strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
                con.commit()

                res = messagebox.askyesnocancel('Notificatrions',
                                                'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id, name), parent=addroot)
                if (res == True):
                    idval.set('')
                    nameval.set('')
                    mobileval.set('')
                    emailval.set('')
                    addressval.set('')
                    genderval.set('')
                    dobval.set('')
            except:
                messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addroot)

        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    #-------------Add student lable------------
    idlable = Label(addroot,text='Enter ID :',bg ='#ffd54f',fg="Black",font = ('times',15, 'bold'),relief=SOLID,borderwidth=1,width=13,anchor="nw")
    idlable.place(x=10, y=40)

    namelable = Label(addroot, text='Enter name :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    namelable.place(x=10, y=100)

    mobilelable = Label(addroot, text='Enter phone :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    mobilelable.place(x=10, y=160)

    emaillable = Label(addroot, text='Enter E-mail :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    emaillable.place(x=10, y=220)

    addresslable = Label(addroot, text='Enter Address :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    addresslable.place(x=10, y=280)

    genderlable = Label(addroot, text='Specify Gender :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    genderlable.place(x=10, y=340)

    doblable = Label(addroot, text='Enter DOB :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    doblable.place(x=10, y=400)

    #-------------------------- Entry boxes --------------------------
    idval = StringVar()
    identry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=idval)
    identry.place(x=190, y=40)

    nameval = StringVar()
    nameentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=nameval)
    nameentry.place(x=190, y=100)

    mobileval = StringVar()
    mobileentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=mobileval)
    mobileentry.place(x=190, y=160)

    emailval = StringVar()
    emailentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=emailval)
    emailentry.place(x=190, y=220)

    addressval = StringVar()
    addressentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=addressval)
    addressentry.place(x=190, y=280)

    genderval = StringVar()
    genderentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=genderval)
    genderentry.place(x=190, y=340)



    dobval = StringVar()
    dobentry = Entry(addroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=dobval)
    dobentry.place(x=190, y=400)

    addbt = Button(addroot, text='Add Student', font=('times', 15, 'bold'), bd=3, relief=SOLID, bg='#ffd54f', fg='Black',
                       activebackground="#c6ff00", activeforeground='#dd2c00',command=addstudent)
    addbt.place(x=180, y=440)
    addroot.mainloop()
#*******************************************************************************************************
#*******************************************************************************************************
#*******************************************************************************************************

# 2nd button Search button

def searchstudent():
    searchroot = Toplevel(master=Dataentryframe)
    searchroot.geometry('500x550+20+140')
    searchroot.grab_set()
    searchroot.title("Search student")
    searchroot.iconbitmap('sql_c.ico')
    searchroot.resizable(False, False)
    searchroot.config(bg='#616161')

    def searchstudent():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif  (name != ''):
            strr = 'select * from studentdata1 where name = %s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        else:
            messagebox.showinfo('Notification','Values does not exist!!!',parent=searchroot)

    #--------------    End for search button --------------------
    # -------------Add student lable------------
    idlable = Label(searchroot, text='Enter ID :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor="nw")
    idlable.place(x=10, y=40)

    namelable = Label(searchroot, text='Enter name :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                      borderwidth=1, width=13, anchor="nw")
    namelable.place(x=10, y=100)

    mobilelable = Label(searchroot, text='Enter phone :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                        relief=SOLID,
                        borderwidth=1, width=13, anchor="nw")
    mobilelable.place(x=10, y=160)

    emaillable = Label(searchroot, text='Enter E-mail :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                       relief=SOLID,
                       borderwidth=1, width=13, anchor="nw")
    emaillable.place(x=10, y=220)

    addresslable = Label(searchroot, text='Enter Address :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                         relief=SOLID,
                         borderwidth=1, width=13, anchor="nw")
    addresslable.place(x=10, y=280)

    genderlable = Label(searchroot, text='Specify Gender :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                        relief=SOLID,
                        borderwidth=1, width=13, anchor="nw")
    genderlable.place(x=10, y=330)

    doblable = Label(searchroot, text='Enter DOB :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                     borderwidth=1, width=13, anchor="nw")
    doblable.place(x=10, y=390)


    datelable = Label(searchroot, text='Enter date :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                     borderwidth=1, width=13, anchor="nw")
    datelable.place(x=10, y=450)

    # -------------------------- Entry boxes --------------------------
    idval = StringVar()
    identry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=idval)
    identry.place(x=190, y=40)

    nameval = StringVar()
    nameentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=nameval)
    nameentry.place(x=190, y=100)

    mobileval = StringVar()
    mobileentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=mobileval)
    mobileentry.place(x=190, y=160)

    emailval = StringVar()
    emailentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=emailval)
    emailentry.place(x=190, y=220)

    addressval = StringVar()
    addressentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=addressval)
    addressentry.place(x=190, y=280)

    genderval = StringVar()
    genderentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=genderval)
    genderentry.place(x=190, y=330)

    dobval = StringVar()
    dobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=dobval)
    dobentry.place(x=190, y=390)

    datebval = StringVar()
    dateentry = Entry(searchroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=datebval)
    dateentry.place(x=190, y=450)

    searchbt = Button(searchroot, text='Search Student', font=('times', 15, 'bold'), bd=3, relief=SOLID, bg='#ffd54f',
                   fg='Black',
                   activebackground="#c6ff00", activeforeground='#dd2c00', command=searchstudent)
    searchbt.place(x=160, y=490)
    searchroot.mainloop()

#*******************************************************************************************************
#*******************************************************************************************************
#*******************************************************************************************************


def deletetudent():
    cc = studenttable.focus() # This is a treeview command which focuses on particular area.
    content  = studenttable.item(cc)      #This will tell us the place means it will firstly search the place where it is and  from cc where we have clicked.
    # In this content we have all details like id, name and address time etc... whole row information. We are using ID for this because ID is unquie.

    pp = content['values'][0]
    strr = 'delete from studentdata1 where id = %s'
    mycursor.execute(strr,(pp))
    con.commit() # This is a necessary details that we have to do.
    messagebox.showinfo('Notification', 'Id {} deleteted sucessfully'.format(pp))
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
#*******************************************************************************************************

def updatestudent():
        def update():
            id = idval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            dob = dobval.get()
            date = datebval.get()
            time = timebval.get()

            strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
            mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
            con.commit()
            messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
            strr = 'select *from studentdata1'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        updateroot = Toplevel(master=Dataentryframe)
        updateroot.geometry('500x600+20+100')
        updateroot.grab_set()
        updateroot.title("Update student")
        updateroot.iconbitmap('sql_c.ico')
        updateroot.resizable(False, False)
        updateroot.config(bg='#616161')


        # -------------Add student lable------------
        idlable = Label(updateroot, text='Update ID :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                        relief=SOLID,
                        borderwidth=1, width=13, anchor="nw")
        idlable.place(x=10, y=40)

        namelable = Label(updateroot, text='Update name :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                          relief=SOLID,
                          borderwidth=1, width=13, anchor="nw")
        namelable.place(x=10, y=100)

        mobilelable = Label(updateroot, text='Update phone :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                            relief=SOLID,
                            borderwidth=1, width=13, anchor="nw")
        mobilelable.place(x=10, y=160)

        emaillable = Label(updateroot, text='Update E-mail :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                           relief=SOLID,
                           borderwidth=1, width=13, anchor="nw")
        emaillable.place(x=10, y=220)

        addresslable = Label(updateroot, text='Update Address :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                             relief=SOLID,
                             borderwidth=1, width=13, anchor="nw")
        addresslable.place(x=10, y=280)

        genderlable = Label(updateroot, text='Update Gender :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                            relief=SOLID,
                            borderwidth=1, width=13, anchor="nw")
        genderlable.place(x=10, y=330)

        doblable = Label(updateroot, text='Update DOB :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                         relief=SOLID,
                         borderwidth=1, width=13, anchor="nw")
        doblable.place(x=10, y=390)

        datelable = Label(updateroot, text='Update date :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                          relief=SOLID,
                          borderwidth=1, width=13, anchor="nw")
        datelable.place(x=10, y=450)

        timelable = Label(updateroot, text='Update time :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'),
                          relief=SOLID,
                          borderwidth=1, width=13, anchor="nw")
        timelable.place(x=10, y=510)

        # -------------------------- Entry boxes --------------------------
        idval = StringVar()
        identry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=idval)
        identry.place(x=190, y=40)

        nameval = StringVar()
        nameentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=nameval)
        nameentry.place(x=190, y=100)

        mobileval = StringVar()
        mobileentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=mobileval)
        mobileentry.place(x=190, y=160)

        emailval = StringVar()
        emailentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=emailval)
        emailentry.place(x=190, y=220)

        addressval = StringVar()
        addressentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=addressval)
        addressentry.place(x=190, y=280)

        genderval = StringVar()
        genderentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=genderval)
        genderentry.place(x=190, y=330)

        dobval = StringVar()
        dobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=dobval)
        dobentry.place(x=190, y=390)

        datebval = StringVar()
        dateentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=datebval)
        dateentry.place(x=190, y=450)

        timebval = StringVar()
        timeentry = Entry(updateroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=30,textvariable=timebval)
        timeentry.place(x=190, y=510)

        updatebt = Button(updateroot, text='Update', font=('times', 15, 'bold'), bd=3, relief=SOLID, bg='#ffd54f',
                       fg='Black',
                       activebackground="#c6ff00", activeforeground='#dd2c00', command=update)
        updatebt.place(x=160, y=550)


        # What we are doing we are getting all the data from treeview to update. Like when we click on id=2 so all data which is filled up in it get stored in then
        # we get all values at update box and we can update this. All data stored in entry boxes.

        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values']
        if (len(pp) != 0):
            idval.set(pp[0])
            nameval.set(pp[1])
            mobileval.set(pp[2])
            emailval.set(pp[3])
            addressval.set(pp[4])
            genderval.set(pp[5])
            dobval.set(pp[6])
            datebval.set(pp[7])
            timebval.set(pp[8])


        updateroot.mainloop()



def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename() # Gives us a path.
    gg = studenttable.get_children()

    # Creating list for storage.
    id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0])
        name.append(pp[1])
        mobile.append(pp[2])
        email.append(pp[3])
        address.append(pp[4])
        dob.append(pp[5])
        gender.append(pp[6])
        addeddate.append(pp[7])
        addedtime.append(pp[8])

    # For exporting a data.
    dd = ['ID','Name','Mobile','E-mail','Address','DOB','Gender','Added date','Added Time'] # Here we are making heading for Excel files.
    df = pandas.DataFrame(list(zip( id, name, mobile, email, address, gender, dob, addeddate, addedtime)), columns   =dd ) # What we are doing we are just pasting the values which is treeview in the file
    paths = r'{}.csv'.format(ff) # Storing in created path, r is readable format.
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel("Notification","Are you want to exit?")
    if (res==True):
        root.destroy()
#----------------------------end ----------------------------------------
#############Function
def connectdb():
    def submitdb():
        global  con, mycursor
        host = hostval.get()
        user = userval.get()
        password = pwval.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Data is incorrect please try again\n'
                                                  '1. Check the username & local host from the SQL database', parent=dbroot)
            return


        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20) ,mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)

            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.geometry('470x260+400+240')
    dbroot.grab_set()
    dbroot.title('Connect database ')
    dbroot.iconbitmap('sql_c.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='#616161')

    def click(event):
        hostentry.config(state=NORMAL)
        hostentry.delete(0,END)
    def click2(event):
        userentry.config(state=NORMAL)
        userentry.delete(0, END)
    def click3(event):
        pwentry.config(state=NORMAL)
        pwentry.delete(0, END)
        pwentry.config(show="*")
    #-------------------------- Connect DB lable ---------------------
    hostlable = Label(dbroot,text='Enter host :',bg ='#ffd54f',fg="Black",font = ('times',15, 'bold'),relief=SOLID,borderwidth=1,width=13,anchor='w')
    hostlable.place(x=10,y=20)

    userlable = Label(dbroot, text='Enter name :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13 ,anchor='w')
    userlable.corner_radius = 5
    userlable.place(x=10, y=90)

    pwlable = Label(dbroot, text='Enter Password :', bg='#ffd54f', fg="Black", font=('times', 15, 'bold'), relief=SOLID,
                    borderwidth=1, width=13, anchor='w')
    pwlable.place(x=10, y=160)

    # -------------------------- Connect DB entry tables ---------------------
    hostval=StringVar()
    hostentry = Entry(dbroot,font = ('times',15, 'bold'),bd=2,relief=SOLID,width=25,textvariable=hostval)
    hostentry.insert(0,"Host name...")
    hostentry.config(state=DISABLED)
    hostentry.bind("<Button-1>",click)
    hostentry.place(x=200,y=20)

    userval = StringVar()
    userentry = Entry(dbroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=25,textvariable=userval)
    userentry.insert(0, "root")
    userentry.config(state=DISABLED)
    userentry.bind("<Button-1>", click2)
    userentry.place(x=200, y=90)

    pwval = StringVar()
    pwentry = Entry(dbroot, font=('times', 15, 'bold'), bd=2, relief=SOLID, width=25,textvariable=pwval)
    pwentry.insert(0, "Password@12")
    pwentry.config(state=DISABLED)
    pwentry.bind("<Button-1>", click3)
    pwentry.place(x=200, y=160)

    connectbt = Button(dbroot,text='Connect',font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black'
                       ,activebackground = "#c6ff00",activeforeground='#dd2c00',command=submitdb)
    connectbt.place(x=180,y=205)

    dbroot.mainloop()



def clocktick():
    time_string = time.strftime(" %H:%M:%S")
    date_string = time.strftime(" %d / %m / %Y")
    clock.config(text= 'Date:' +date_string +"\n" +'Time' +time_string, fg = "#311b92")
    clock.after(100,clocktick)

######### Slider Intro ########
import random
colour = ['red','green','blue','black','purple']
def introlablecolortick():
    fg = random.choice(colour)
    sliderlable.config(fg=fg)
    sliderlable.after(400,introlablecolortick)

def introlabel():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        sliderlable.config(text = text)
    else:
        text = text+ss[count]
        sliderlable.config(text = text)
        count+=1
    sliderlable.after(200,introlabel)


from tkinter import *
import time
from tkinter import Toplevel,messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
import pandas

root = Tk()
root.title("Student Management System")
root.config(bg = "Black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

root.iconbitmap("Student.ico")

############################## FRAMES ###########################
Dataentryframe = Frame(root,bg = "#90a4ae",relief = SOLID,borderwidth=5)
Dataentryframe.place(x = 5, y = 80, width = 400, height=600)

#-----------------------------------  Buttons ---------------------------

addbtn = Button(Dataentryframe, text="Add Student", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=addstudent )
image = Image.open("Images/Add.png")
image = image.resize((32,32))
photo = ImageTk.PhotoImage(image)
b_label = Label(image=photo)
b_label.place(x=335,y=107)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(Dataentryframe, text="Search Student", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=searchstudent )
image2 = Image.open("Images/search.jpg")
image2 = image2.resize((32,32))
photo2 = ImageTk.PhotoImage(image2)
b_label2 = Label(image=photo2)
b_label2.place(x=335,y=193)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(Dataentryframe, text="Delete Entry", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=deletetudent )
image3 = Image.open("Images/delete.jpg")
image3 = image3.resize((32,32))
photo3 = ImageTk.PhotoImage(image3)
b_label3 = Label(image=photo3)
b_label3.place(x=335,y=279)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(Dataentryframe, text="Update database", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=updatestudent )
image4 = Image.open("Images/update.jpg")
image4 = image4.resize((32,32))
photo4 = ImageTk.PhotoImage(image4)
b_label4 = Label(image=photo4)
b_label4.place(x=335,y=361)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(Dataentryframe, text="Show All", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=showstudent )
image5 = Image.open("Images/show.jpg")
image5 = image5.resize((32,32))
photo5 = ImageTk.PhotoImage(image5)
b_label5 = Label(image=photo5)
b_label5.place(x=335,y=445)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(Dataentryframe, text="Export data", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=exportstudent )
image6 = Image.open("Images/export.jpg")
image6 = image6.resize((32,32))
photo6 = ImageTk.PhotoImage(image6)
b_label6 = Label(image=photo6)
b_label6.place(x=335,y=530)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(Dataentryframe, text="Exit", width=20, font=('times', 15, 'bold'),bd=3, relief=SOLID,bg='#ffd54f',fg='Black',activebackground = "#c6ff00",activeforeground='#dd2c00',command=exitstudent )
image7 = Image.open("Images/exit.jpg")
image7 = image7.resize((32,32))
photo7 = ImageTk.PhotoImage(image7)
b_label7= Label(image=photo7)
b_label7.place(x=335,y=616)
exitbtn.pack(side=TOP,expand=True)

#-----------------------------------------------------------------------------------------------------------------------


showdataframe = Frame(root,bg = "white",relief = SOLID,borderwidth=5)
showdataframe.place(x = 440, y = 80, width = 920, height=600)

#------------------------- show data labels -------------------------------
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',15,'bold'),foreground='#d50000')
style.configure('Treeview',font=('times',15),background='Black',foreground='white')
scroll_x= Scrollbar(showdataframe,orient=HORIZONTAL)
scroll_y= Scrollbar(showdataframe,orient=VERTICAL)
studenttable = Treeview(showdataframe, columns = ('ID','Name','Mobile No.','E-mail','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('E-mail',text='E-mail')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'

#Size change of columns

studenttable.column('ID',width=80)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('E-mail',width=200)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=120)
studenttable.column('Added Date',width=120)
studenttable.column('Added Time',width=120)




studenttable.pack(fill=BOTH,expand=1)





############################## Slider ###########################

ss = "Welcome to student management system"
count = 0
text = ''
sliderlable = Label(root,bg= "#ffd54f",font = ("console", 20, "bold"),text = ss,relief=RIDGE,width=35,borderwidth=2)
sliderlable.place(x = 410,y=0)
introlabel()
introlablecolortick()

############################## Clock ###########################

clock = Label(root,bg= "#ffd54f",font = ("console", 11, "bold"),borderwidth=2,width = 25,height=2,relief=RIDGE)
clock.place(x=0,y=0)
clocktick()

############################## Clock ###########################

connecttodatabase = Button(root, text='Connect to database',height=2,borderwidth=2,font = ("console", 11 , "bold"),bg= "#ffd54f",fg="#311b92",relief=RIDGE,
                           activebackground = "#c6ff00",activeforeground='#dd2c00',command=connectdb)
connecttodatabase.place(x=1198,y=0)











































root.mainloop()



