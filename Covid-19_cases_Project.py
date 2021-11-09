def Scrap():
    def notifyme(title,message):
        plyer.notification.notify(
            title=title,
            message=message,
            app_icon = 'pg.ico',
            timeout = 20
        )
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    tablebody = soup.find('tbody')
    ttt = tablebody.find_all('tr')
    notifyCountry = countrydata.get()
    if (notifyCountry == ''):
        notifyCountry= 'india'

    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases = [], [], [], [], [], [], []
    serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion = [], [], [], [], []
    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
               'serious', 'totalcases_permillion', 'totaldeaths_permillion', 'totaltests', 'totaltests_permillion']
    for i in ttt:
        id = i.find_all('td')
        if(id[1].text.strip().lower() == notifyCountry):
            totalcases1 = int(id[2].text.strip().replace(',',''))
            totaldeaths1 = id[4].text.strip()
            newcases1 = id[3].text.strip()
            newdeaths1 = id[5].text.strip()
            notifyme('Corona virus details in {}'.format(notifyCountry),'Total Cases:{}\nTotal deaths :{},\nNew Cases :{},\nNew Deaths :{}'.format(totalcases1,totaldeaths1,newcases1,newdeaths1))


        countries.append(id[1].text.strip())
        total_cases.append(int(id[2].text.strip().replace(',',  '')))
        new_cases.append(id[3].text.strip())
        total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious.append(id[8].text.strip())
        totalcases_permillion.append(id[9].text.strip())
        totaldeaths_permillion.append(id[10].text.strip())
        totaltests.append(id[11].text.strip())
        totaltests_permillion.append(id[12].text.strip())
    df = pd.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,
                               serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion)),columns=headers)
    sor = df.sort_values("total_cases",ascending=False)
    for k in formatlist:
        if(k=='html'):
            path2 = '{}/alldata.html'.format(path)
            sor.to_html(r'{}'.format(path2))
        if (k == 'json'):
            path2 = '{}/alldata.json'.format(path)
            sor.to_json(r'{}'.format(path2))
        if (k == 'csv'):
            path2 = '{}/alldata.csv'.format(path)
            sor.to_csv(r'{}'.format(path2))
    if (len(formatlist)!=0):
        messagebox.showinfo("Notification","Corona record is saved{}".format(path2),parent=root )
def inhtml():
    formatlist.append('html')
    InHtml.configure(state = "disabled")
def injson():
    formatlist.append('json')
    InJson.configure(state = "disabled")
def incsv():
    formatlist.append('csv')
    InCsv.configure(state = "disabled")

def download():
    global path
    if(len(formatlist)!=0):
        path = filedialog.askdirectory()
        print(path)
    else:
        pass
    Scrap()
    formatlist.clear()
    InHtml.configure(state = 'normal')
    InJson.configure(state='normal')
    InCsv.configure(state='normal')



import requests
from bs4 import BeautifulSoup
import plyer
from tkinter import *
from tkinter import messagebox,filedialog
import pandas as pd
root = Tk()
root.title("Corona virus Information")
root.geometry("530x300+200+80")
root.config(bg= "black")
root.iconbitmap("pg.ico")
formatlist = []
path = ''
################################   Label #######################################

IntoLabel = Label(root,text = "Corona Virus info", font=("roman",30,"bold"),bg="Gray",width=22)
IntoLabel.pack(fill="x")

EntryLabel = Label(root,text = "Notify contry =",fg = "White", font=("roman",20,"bold"),bg="Black")
EntryLabel.place(x=10,y=70)

FormatLabel = Label(root,text = "Download in = ",fg = "White", font=("roman",20,"bold"),bg="Black")
FormatLabel.place(x=10,y=150)

#################################  Entry #################################
countrydata =StringVar()
ent1 = Entry(root,textvariable=countrydata, font=("roman",20,"bold"),relief = "sunken",bd=2,width = 20)
ent1.place(x = 210,y=70)

############################## Buttons #######################

InHtml = Button(root,text="HTML",bg = "#b2ff59", font=("ariel",15,"bold"),relief = "sunken",activebackground="#ffd54f",activeforeground="blue"
                ,bd=2,width=5,command = inhtml)
InHtml.place(x=210,y=150)

InJson = Button(root,text="JSON",bg = "#b2ff59", font=("ariel",15,"bold"),relief = "sunken",activebackground="#ffd54f",activeforeground="blue"
                ,bd=2,width=5,command = injson)
InJson.place(x=320,y=150)

InCsv = Button(root,text="CSV",bg = "#b2ff59", font=("ariel",15,"bold"),relief = "sunken",activebackground="#ffd54f",activeforeground="blue"
                ,bd=2,width=5,command = incsv)
InCsv.place(x=430,y=150)

submit = Button(root,text="Submit",bg = "#ffff00",fg="red", font=("ariel",15,"bold"),relief = "sunken",activebackground="#ffd54f",activeforeground="blue"
                ,bd=2,width=25,command = download)
submit.place(x=110,y=250)

###########################################  Scrapping the data #########################



root.mainloop()