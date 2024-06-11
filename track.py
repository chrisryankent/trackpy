from ttkbootstrap import *
import ttkbootstrap as tb
from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

root =tb.Window("Phone Tracking",themename="superhero")
root.geometry(("950x500"))
root.resizable(False,False)

def track():
    pass
my_label =tb.Label(root,text="Track your relative, friend, lover with Kent",bootstyle="danger",
font=("TimesNewRoman",20)).grid(row=0,column=0,columnspan=2)

my_frame =tb.Frame(root)
my_frame.grid(column=0,row=1,padx=10)


my_frame1 = tb.Frame(root,pad=20)
my_frame1.grid(column=1,row=1)

def track():
    global number
    global geocoder
    global yourLocation
    global  yourServiceProvider
    global results
    global query
    global phoneNumber
    number= (entery3.get())
    phoneNumber = phonenumbers.parse(number)
    yourLocation = geocoder.description_for_number(phoneNumber,"en")
    yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
    geocoder = OpenCageGeocode(str(entery1.get()))
    query = str(yourLocation)
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    label =tb.Label(my_frame,text= f"{lat} {lng}",bootstyle="danger")
    label.grid(row=1,column=1)
    label1 =tb.Label(my_frame,text= f"{yourLocation} {yourServiceProvider}",bootstyle="danger")
    label1.grid(row=2,column=1)
    

def click_bind(e):
    if my_combo.get()==country[0]:
        code = "+256"
        entery3.delete(0,END)
        entery3.insert(0, code)
    elif my_combo.get()==country[1]:
        code = "+254"
        entery3.delete(0,END)
        entery3.insert(0,code) 
    elif my_combo.get()==country[2]:
        code ="+253"
        entery3.delete(0,END)
        entery3.insert(0,code)
    elif my_combo.get()==country[3]:
        code ="+252"
        entery3.delete(0,END)
        entery3.insert(0,code) 
    else :
        code ="+251"
        entery3.delete(0,END)
        entery3.insert(0,code)     

country= ["Uganda",
"Kenya", 
"Tanzania",
"Rwanda",
"Burundi"]
mylabel =tb.Label(my_frame,text="Procedures",bootstyle="default",
font=("TimesNewRoman",12)).grid(row=0,column=0)
people = ["Get Geoapi By signing in to https://opencagedata.com/api", "This will Give you an approximated Location","Copy Displayed cordinates into Google and open Maps"]
for x in people:
    mylabe =tb.Label(my_frame,text=x,bootstyle="success",pad=2,wraplength=300,font=(20),justify="left").grid(padx=20,pady=20)
   



mylabel1 =tb.Label(my_frame1,text="Enter your Api Key",bootstyle="default",
font=("TimesNewRoman",12),pad=45).grid(row=0,column=0)
entery1 = tb.Entry(my_frame1,bootstyle=("success"),width=30)
entery1.grid(row=0,column=1)

mylabel2 =tb.Label(my_frame1,text="Choose your Country",bootstyle="default",
font=("TimesNewRoman",12),pad=45).grid(row=1,column=0)
my_combo= tb.Combobox(my_frame1,values=country,bootstyle="success")
my_combo.grid(row=1,column=1)

mylabel3 =tb.Label(my_frame1,text="Enter your Number",bootstyle="default",
font=("TimesNewRoman",12),pad=45).grid(row=2,column=0)
entery3 = tb.Entry(my_frame1,bootstyle=("success"),width=30)
entery3.grid(row=2,column=1)

my_button= tb.Button(my_frame1,text="track",bootstyle=("outline,success"),width=10,command=track).grid(row=3,column=1)
code=""




 
my_combo.bind("<<ComboboxSelected>>", click_bind)  
# number= ((entery3.get()))
# phoneNumber = phonenumbers.parse(number)
# yourLocation = geocoder.description_for_number(phoneNumber,"en")
# yourServiceProvider = carrier.name_for_number(phoneNumber,"en")  
# label =tb.Label(my_frame,text= f"{yourLocation | yourServiceProvider}")
# label.grid(row=1,column=1)   












root.mainloop()
