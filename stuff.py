# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:47:17 2017

@author: andrasz
"""

from tkinter import *
import basedata
import coredb

#***###################################################***#
def startmodule(x):
    
#
#-optDict[] ruft eine der def() aus dem dict auf
#-newsearchbox looks like [1, searchobject, dbC 1/0, dbA 1/0, dbM 1/0]
#
    
    print ('...loading: startmodule()')
        
    """newsearchbox looks like [1, searchobject, dbC 1/0, dbA 1/0, dbM 1/0]"""
    optionX = x[0]
    optDict = {1 : getting_a_list,
               2 : coredb.get_everything,
               3 : material,
               }
    print ('...Parameter: ', x)
    return optDict[optionX](x)
#***###################################################***#


def getting_a_list(xlst):
    
    print (xlst[1])
    x = []
    if xlst[2] == 1:
        x.append(coredb.get_stuff_by_type([1, xlst[1]]))
    
    elif xlst[2] == 1:
        x.append(coredb.get_stuff_by_type([2, xlst[1]]))
    
    elif xlst[2] == 1:
        x.append(coredb.get_stuff_by_type([3, xlst[1]]))
    print (x)
    return x


def herewego(x):
# x number of entries, y = choice in decider box
    print ('...loading: herewego module')
    global newstuff 
    newstuff = basedata.Stammdaten()
    chooser(x)
    optionX = x[0]
    optDict = {1 : coredb.insert_newcustomer,
               2 : coredb.insert_newarticle,
               3 : coredb.insert_newmaterial,
               }
    optDict[optionX](newstuff)
    
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

def article(data):
    
    print ('...loading: article()') 
    
    newstuff.name = data[1]
    newstuff.intID = data[2]
    newstuff.extID = data[3]
#    newstuff.manufacturing = 
#    newstuff.tbm = 
    newstuff.ppcent = data[4]
#    newstuff.mincost = ]
    newstuff.weight = data[5]
#    newstuff.dimensions = 
    newstuff.material = data[6]
#    newstuff.stock = 
    
def material(data):
    
    print ('...loading: material()')
    
    newstuff.name = data[1]
    newstuff.company = data[2]
    newstuff.price = data[3]


"""***                        -ENTRY BOXES-                           ***"""


def newcustomerbox():
    
    print ('...loading: new customer input box')
    
    box = Tk()
    box.geometry("600x300")
    box.title("New Customer")
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
    emailE.insert(0, "peterdermeter@gmx.de")
    emailE.grid(row=3, column=1)
    
    #OK Button
    insertButt = Button(box, text="Confirm")
    insertButt.grid(row=4, column=0)
    insertButt.config(command = lambda: [x.append(nameE.get()), 
                                         x.append(addressE.get()),
                                         x.append(emailE.get()),
                                         herewego(x), box.destroy()])
    

def newarticlebox():
    
    print ('...loading: new article input box')
    
    box = Tk()
    box.geometry("600x300")
    box.title("New Article")
    # x[0] = 2 für article in Stammdaten
    x = [2]
    
    #Labels
    nameL = Label(box, text='Article Type: ')
    nameL.grid(row=1, column=0, sticky=E)
    intIDL  = Label(box, text='internal ID: ')
    intIDL.grid(row=2, column=0, sticky=E)
    extIDL  = Label(box, text='External ID: ')
    extIDL.grid(row=3, column=0, sticky=E)
    ppcL  = Label(box, text='Price (/100 parts): ')
    ppcL.grid(row=4, column=0, sticky=E)
    weightL  = Label(box, text='Weight (in gr.): ')
    weightL.grid(row=5, column=0, sticky=E)
    materialL = Label(box, text='Material: ')
    materialL.grid(row=6, column=0, sticky=E)
    
    #Entry boxes
    nameE = Entry(box)
    nameE.delete(0, END)
    nameE.insert(0, "Stopfen")
    nameE.grid(row=1, column=1)
    
    intIDE = Entry(box)
    intIDE.delete(0, END)
    intIDE.insert(0, "1337")
    intIDE.grid(row=2, column=1)

    extIDE = Entry(box)
    extIDE.delete(0, END)
    extIDE.insert(0, "Z192")
    extIDE.grid(row=3, column=1)
    
    ppcE = Entry(box)
    ppcE.delete(0, END)
    ppcE.insert(0, 6.80)
    ppcE.grid(row=4, column=1)
    
    weightE = Entry(box)
    weightE.delete(0, END)
    weightE.insert(0, 25.7)
    weightE.grid(row=5, column=1)
    
    materialE = Entry(box)
    materialE.delete(0, END)
    materialE.insert(0, "PTFE")
    materialE.grid(row=6, column=1)
    
    #OK Button
    insertButt = Button(box, text="Confirm")
    insertButt.grid(row=7, column=0)
    insertButt.config(command = lambda: [x.append(nameE.get()), 
                                         x.append(intIDE.get()),
                                         x.append(extIDE.get()),
                                         x.append(ppcE.get()),
                                         x.append(weightE.get()),
                                         x.append(materialE.get()),
                                         herewego(x), box.destroy()])

    
def newmaterialbox():
    
    print ('...loading: new materialinput box')
    
    box = Tk()
    box.geometry("600x300")
    box.title("New Material")
    
    # x[0] = 3 for new material in db
    x = [3]
    
    #Labels
    nameL = Label(box, text='Material Name: ')
    nameL.grid(row=1, column=0, sticky=E)
    c_nameL = Label(box, text='Company Name: ')
    c_nameL.grid(row=2, column=0, sticky=E)
    priceL = Label(box, text='Price (per kg): ')
    priceL.grid(row=3, column=0, sticky=E)
    
    #Entry boxes
    nameE = Entry(box)
    nameE.delete(0, END)
    nameE.insert(0, "PTFE")
    nameE.grid(row=1, column=1)
    
    c_nameE = Entry(box)
    c_nameE.delete(0, END)
    c_nameE.insert(0, "Google Inc.")
    c_nameE.grid(row=2, column=1)
    
    priceE = Entry(box)
    priceE.delete(0, END)
    priceE.insert(0, 16.82)
    priceE.grid(row=3, column=1)
    
    #OK Button
    insertButt = Button(box, text="Confirm")
    insertButt.grid(row=4, column=0)
    insertButt.config(command = lambda: [x.append(nameE.get()), 
                                         x.append(c_nameE.get()),
                                         x.append(priceE.get()),
                                         herewego(x), box.destroy()])
    
def newsearchbox1():
    box = Tk()
    toplvl = Checkbox(box)


class Checkbox:
    
    def __init__(self, master):
        
        print ('...loading: new search box')
        
        self.x=[]
        
        master.geometry("600x300")
        master.title("Weird Checkbox template")
        
        #Labels
        self.searchL = Label(master, text='Search for: ')
        self.searchL.grid(row=1, column=0, sticky=E)
        self.searchL = Label(master, text='Check following DBs: ')
        self.searchL.grid(row=3, column=0, sticky=E)
        
        #Entry boxes
        self.searchE = Entry(master)
        self.searchE.delete(0, END)
        self.searchE.insert(0, "PTFE")
        self.searchE.grid(row=2, column=1)
        
        #Checkbuttons
        self.checkVar1 = IntVar(master)
        checkbuttonC = Checkbutton(master, text = "Customers", variable = self.checkVar1)
        checkbuttonC.grid(row=3, column=1,)
        checkbuttonC.select()
        
        self.checkVar2 = IntVar(master)
        checkbuttonA = Checkbutton(master, text = "Articles", variable = self.checkVar2)
        checkbuttonA.grid(row=3, column=2,)
        checkbuttonA.select()
        
        self.checkVar3 = IntVar(master)
        self.checkbuttonM = Checkbutton(master, text = "Materials", variable = self.checkVar3)
        self.checkbuttonM.grid(row=3, column=3,)
        self.checkbuttonM.select()
        
        #Search Button
        searchButt = Button(master, text="Confirm")
        searchButt.grid(row=4, column=0)
#        self.searchButt.config(command = lambda: [self.checkem(self.checkVar1.get(), self.checkVar2, self.checkVar2)])
        searchButt.config(command = lambda: [self.checkem()])
    
    
    def checkem(self):

        print ("variable1 is ", self.checkVar1.get())
        print ("variable2 is ", self.checkVar2.get())
        print ("variable3 is ", self.checkVar3.get())