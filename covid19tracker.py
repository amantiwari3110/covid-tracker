import requests
from bs4 import*
from tkinter import*
from PIL import Image,ImageTk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

#from win32com.client import Dispatch
#speaker=Dispatch('SAPI.SpVoice')
#speaker.Speak("Hey geeks ! welcome to Aman's covid 19 tracker app")

def get_html_data(url):
    data=requests.get(url)
    return data

def get_covid_data():
    url='https://www.worldometers.info/coronavirus/'
    html_data=get_html_data(url)
    bs=BeautifulSoup(html_data.text,'html.parser')
    info_div=bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")

    all_data=""     #it is empty string for storing data.

    for block in info_div:
        #<h1>Coronavirus Cases:</h1>
        text=block.find("h1",class_=None).get_text()     # find coronavirus cases.
        #<span style="color:#aaa">72,126,781 </span>  
        count=block.find("span",class_=None).get_text()  #for counting coronavirus cases in numbers.
        all_data=all_data + text + " " + count + "\n"
    #print(all_data)
    return all_data

def get_country_data():
    name=textfield.get()
    url='https://www.worldometers.info/coronavirus/country/' + name
    html_data=get_html_data(url)
    bs=BeautifulSoup(html_data.text,'html.parser')
    info_div=bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")

    all_data=""     #it is empty string for storing data.

    for block in info_div:
        #<h1>Coronavirus Cases:</h1>
        text=block.find("h1",class_=None).get_text()     # find coronavirus cases.
        #<span style="color:#aaa">72,126,781 </span>  
        count=block.find("span",class_=None).get_text()  #for counting coronavirus cases in numbers.
        all_data=all_data + text + " " + count + "\n"
    main_label['text']=all_data

def reload():
    #for store new data
    new_data=get_covid_data()
    #updated data here
    main_label['text']=new_data


get_covid_data()

root=Tk()
root.title("COVID 19 TRACKER")
Title_label=Label(text="Welcome to Covid 19 Tracker Application"
,fg="red",bg='black',font='comicsansms 20 bold',borderwidth=18,relief=SUNKEN)
Title_label.pack(fill=X)
f=("poppins",25,"bold")                        #poppins is a font style name..
root.geometry("633x700")
root.minsize(750,850)
#root.configure(background="red")
#icon for project covid 19 tracker.
root.iconbitmap("coronavirus_QT2_icon.ico")

banner=Image.open('coronavirus.png')
resized=banner.resize((200,200),Image.ANTIALIAS)
ima=ImageTk.PhotoImage(resized)
#normal image size is 500x375
banner_label=Label(root,image=ima)
banner_label.pack(pady=25)

#We can write country name here.........
large_font=('Verdana',24)
textfield_var=StringVar(value='Enter Country Name Here !')
textfield=Entry(root,textvariable=textfield_var,font=large_font,width=24,relief=RAISED,borderwidth=6,fg='green')
textfield.pack()

'''
textfield=Entry(root,text="enter here",relief=GROOVE,font="comicsansms 16 bold")
textfield.pack(ipady=10)
'''

#SHOW OUR DATA INSIDE TKINTER WINDOW ...
main_label=Label(root,text=get_covid_data(),font=f)
main_label.pack()

#Button for get data/retrieve data..
#relief must be flat, groove, raised, ridge, solid, or sunken
get_button=Button(root,text="Get Data",font="comicsansms 20 bold",relief=SUNKEN,borderwidth=8,
fg='red',command=get_country_data)
get_button.pack()

#Button for reload data..
#relief must be flat, groove, raised, ridge, solid, or sunken
reload_button=Button(root,text="Reload",font="comicsansms 20 bold",relief=SUNKEN,borderwidth=8,
fg='red',command=reload)
reload_button.pack()

#direct close button..
close_button=Button(root,text='Close',font="comicsansms 20 bold",relief=SUNKEN,borderwidth=8,
fg='red',command=root.destroy).pack()

root.mainloop()
print("Aman")
