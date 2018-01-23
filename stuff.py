# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:47:17 2017

@author: andrasz
"""

from tkinter import *
import basedata
import coredb

def startmodule(x):
    # optDict[] ruft eine der def() aus dem dict auf 
        
    print ('...loading: startmodule()')
        
    optionX = x[0]
    optDict = {1 : getting_a_list,
               2 : article,
               3 : material,
               }
    return optDict[optionX]('2P GmbH')


def getting_a_list(somethingGud):
    return coredb.get_stuff_by_name(somethingGud)
    

def herewego(x):
# x number of entries, y = choice in decider box
    storage = x
    global newstuff 
    newstuff = basedata.Stammdaten()

    chooser(x)
    
    coredb.insert_stuff(newstuff)
    
    print ("Le FIN")
    

    
def chooser(data):
    
# optDict[] ruft eine der def() aus dem dict auf 
        
    print ('...loading: chooser()') 
        
    optionX = data[0]
    optDict = {1 : customer,
               2 : article,
               3 : material,
               }
    optDict[optionX](data)

def customer(data):
    
    print ('...loading: customer()') 
    
    newstuff.name = data[1]
    newstuff.address = data[2]
    newstuff.email = data[3]

def article():
    
    print ('...loading: article()') 
    
    newstuff.interneBez = 0
    newstuff.externeBez = 0
    newstuff.weight = 0
    newstuff.manufacturing = 0
    newstuff.zufertigen = 0
    newstuff.ppcent = 0
    newstuff.mincost = 0
    newstuff.dimensions = 0
    newstuff.material = 0
    newstuff.stock = 0
    
def material():
    
    print ("-bdata/material")
    
    newstuff.company = 0
    newstuff.price = 0

def newcustomer():
    
    print ('-new customer input box')
    
    box = Tk()
    box.geometry("600x300")
    
    # x = list for data
    x = [1]
    
    #Labels
    nameL = Label(box, text='Company Name: ')
    nameL.grid(row=1, column=0, sticky=E)
    addressL = Label(box, text='Company Address: ')
    addressL.grid(row=2, column=0, sticky=E)
    emailL = Label(box, text='Email contact: ')
    emailL.grid(row=3, column=0, sticky=E)
    
    #Entry boxes
    nameE = Entry(box)
    nameE.delete(0, END)
    nameE.insert(0, "2P GmbH")
    nameE.grid(row=1, column=1)
    
    addressE = Entry(box)
    addressE.delete(0, END)
    addressE.insert(0, "34346 HMü")
    addressE.grid(row=2, column=1)
    
    emailE = Entry(box)
    emailE.delete(0, END)
    emailE.insert(0, 1300)
    emailE.grid(row=3, column=1)
    
    #OK Button
    insertButt = Button(box, text="Confirm")
    insertButt.grid(row=4, column=0)
    insertButt.config(command = lambda: [x.append(nameE.get()), 
                                         x.append(addressE.get()),
                                         x.append(emailE.get()),
                                         herewego(x), box.destroy()])
    

def newarticle():
    
    print ('new article input box')
    
    box = Tk()
    box.geometry("600x300")
    # x = 2 für article in Stammdaten
    x = 2
    
    #Labels
    nameL = Label(box, text='Article Name: ')
    nameL.grid(row=1, column=0, sticky=E)
    dimensionsL = Label(box, text='Product dimensions: ')
    dimensionsL.grid(row=2, column=0, sticky=E)
    materialL = Label(box, text='Material: ')
    materialL.grid(row=3, column=0, sticky=E)
    stockL = Label(box, text='Stock: ')
    stockL.grid(row=4, column=0, sticky=E)
    
    #Entry boxes
    nameE = Entry(box)
    nameE.grid(row=1, column=1)
    dimensionsE = Entry(box)
    dimensionsE.grid(row=2, column=1)
    materialE = Entry(box)
    materialE.grid(row=3, column=1)
    stockE = Entry(box)
    stockE.grid(row=4, column=1)
    
    #OK Button
    insertButt = Button(box, text="Confirm")
    insertButt.grid(row=5, column=0)
    insertButt.config(command=lambda: [box.destroy()])
    #company = Stammdaten.Stammdaten(nameE.get())
    
