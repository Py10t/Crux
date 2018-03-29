# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

from tkinter import *
import stuff
import os
from Zeichnungen import *
import basedata
from tkinter import filedialog


class Enginedisplayer:
    
    def __init__(self):
        
        engineframe = Toplevel(toplvl.mainframe)
        engineframe.geometry("300x400")
        engineframe.title("Engine 1")
    
        #Labels
        StatusL = Label(engineframe, text='Engine Status : ')
        StatusL.grid(row=1, column=0, sticky=E)
        ArticleL = Label(engineframe, text='Article : ')
        ArticleL.grid(row=2, column=0, sticky=E)
        StartL = Label(engineframe, text='Start (d/m/y - time) : ')
        StartL.grid(row=3, column=0, sticky=E)
        EndL = Label(engineframe, text='End (d/m/y - time) : ')
        EndL.grid(row=5, column=0, sticky=E)
        
        StatusL2 = Label(engineframe, text='Online', fg="green")
        StatusL2.grid(row=1, column=1, sticky=E)
        Article2 = Label(engineframe, text='3K - 380248')
        Article2.grid(row=2, column=1, sticky=E)
        StartL2 = Label(engineframe, text='30.03.2018')
        StartL2.grid(row=3, column=1, sticky=E)
        StartL3 = Label(engineframe, text='8:00')
        StartL3.grid(row=4, column=1, sticky=E)
        EndL2 = Label(engineframe, text='05.04.2018')
        EndL2.grid(row=5, column=1, sticky=E)
        EndL2 = Label(engineframe, text='18:00')
        EndL2.grid(row=6, column=1, sticky=E)
        
        button = Button(engineframe, text = "Open TD", command = self.openfile)
        button.grid(column = 0, row = 0)
        
    def openfile(self):
        return filedialog.askopenfilename()
        
def display_engines():
    
    print ('...loading: display_machines')
    
    box = Enginedisplayer()
    
def doNothing():
    print(toplvl.x)
    
def newdata():
    
    print ('...loading: newdata() button box')
    
    w = "First box"
    x = ["Customer", "Article", "Material"]
    y = [stuff.newcustomerbox, stuff.newarticlebox, stuff.newmaterialbox]
    newbox = basedata.Basic_box(w, x, y)
    
def newstockbuttons():
    
    print ('...loading: newstockbuttons()')
    
    w = "Second box"
    x = ["Customer", "Article", "Material"]
    y = [lambda: displaydb([2, 1]), lambda: displaydb([2, 2]), lambda: displaydb([2, 3])]
    newbox = basedata.Basic_box(w, x, y)


def displayframe():
# ***** Right frame ****
        
        
        toplvl.displayframe = Frame(toplvl.mainframe)
        toplvl.displayframe.pack(fill=Y, expand=True)
        toplvl.displayframe.place(relx=0.47, rely=0.01, relheight=0.98, relwidth=0.53)
        toplvl.displayframe.configure(relief=GROOVE)
        toplvl.displayframe.configure(background="#000000")
        toplvl.displayframe.configure(highlightbackground="#000000")
        toplvl.displayframe.configure(highlightcolor="black")


def displaydb(x):
#iterates through a list retrieved from db and displays it in rframe
    
    print ('...loading: showdb()')
    
    lst = stuff.startmodule(x)
    
    displayframe()
    
    dbdisplay = Text(toplvl.displayframe)
       
    for x in lst:
        dbdisplay.insert(END, str(x) + '\n')
    
    dbdisplay.pack()
    
    print ('db listed in rframe')


class Crux:
    
    def __init__(self, master):
# ***** Main Menu *****
        
        
        master.geometry("800x600+834+103")
        master.title("Crux")
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")
        #"tearOff=False" globally removes dashed lines in the drop down
        master.option_add('*tearOff', False)
        
        self.x = 'something something'

        self.menu = Menu(master)
        master.configure(menu=self.menu)

        #  "File" 
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="New Project ...", command=doNothing)
        self.subMenu.add_command(label="New", command=doNothing)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=master.destroy)

        #  "Edit"
        #self.menu.add_cascade(label="Edit", menu=self.subMenu)
        #self.editMenu.add_command(label="Redo", command=doNothing)


# ***** Toolbar *****


        self.toolbar = Frame(master, bg="grey")
        self.insertButt = Button(self.toolbar, text="New(Demo)", command=lambda:[newdata()])
        self.insertButt.pack(side=LEFT, padx=2, pady=2)
        self.printButt = Button(self.toolbar, text="Search", command=lambda:[stuff.newsearchbox1()])
        self.printButt.pack(side=LEFT, padx=2, pady=2)
        self.stockButt = Button(self.toolbar, text="Stock", command=lambda:[newstockbuttons()])
        self.stockButt.pack(side=LEFT, padx=2, pady=2)
        self.machinesButt = Button(self.toolbar, text="Engines", command=lambda:[display_engines()])
        self.machinesButt.pack(side=LEFT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X)


# ***** Statusbar *****


        self.status = Label(master, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

        
# ***** Mainframe *****
        
        
        self.mainframe = Frame(master)
        self.mainframe.configure(background="#d9d9d9")
        self.mainframe.pack(side=TOP, fill=BOTH, expand=True)
        
        
# ***** Right frame ****
        
        
        self.displayframe = Frame()
#        self.rframe = Frame(self.mainframe)
#        self.rframe.pack(fill=Y, expand=True)
#        self.rframe.place(relx=0.47, rely=0.01, relheight=0.98, relwidth=0.53)
#        self.rframe.configure(relief=GROOVE)
#        self.rframe.configure(background="#000000")
#        self.rframe.configure(highlightbackground="#000000")
#        self.rframe.configure(highlightcolor="black")
        
        

   
#def start_gui():
    #global val, w, root
root = Tk()
toplvl = Crux (root)

root.mainloop()
