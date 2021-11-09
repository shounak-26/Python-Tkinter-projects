from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

folder_name = ""

def openLocation():
    global folder_name
    folder_name = filedialog.askdirectory()

    if (len(folder_name)>1):
        locationError.config(text=folder_name,fg="Green")
    else:
        locationError.config(text="Please choose path...",fg="red")


def downloadvideo():
    choice =ytdchoices.get()
    url=ytdEntry.get()
    yt = YouTube(url)

    if (choice == choices[0]):
        select = yt.streams.filter( res="720p",progressive=True, type="video").first()

    elif (choice == choices[1]):
        select = yt.streams.filter( res="480p", progressive=True,type="video").last()

    elif (choice == choices[2]):
        select = yt.streams.filter(res="360p",progressive=True, type="video").last()

    elif (choice == choices[3]):
        select = yt.streams.filter(progressive=True, file_extension='mp4').last()

    elif (choice == choices[4]):
        select = yt.streams.filter(only_audio=True).first()

    else:
        ytdError.config(text="Paste Link again!!", fg="red")

    #download function
    select.download(folder_name)
    ytdError.config(text="Download Completed!!")

root = Tk()
root.title("YTD Downloader")
root.geometry("400x450") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Heading
l1 = Label(text="YouTube video downloader",font="3ds 20 bold").pack()
l2 = Label(text="Drop-down the link below",font="3ds 16 bold").pack()

#Entry box

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.pack()

#Error Msg
ytdError = Label(root,text="Error Msg",fg="red",font="3ds 12")
ytdError.pack()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("3ds 12 bold "))
saveLabel.pack(pady=5)

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.pack()

#Error Msg location
locationError = Label(root,text="Error Msg of Path",fg="red",font="3ds 12")
locationError.pack()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("3ds 12 "))
ytdQuality.pack(pady=5)

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.pack()

#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=downloadvideo)
downloadbtn.pack(pady=20)

root.mainloop()