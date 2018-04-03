# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

from tkinter import *
import stuff
import os
import basedata
from tkinter import filedialog


class Machine_planning:
    
    def __init__(self):
        
        toplvl.leftframe = Frame(toplvl.mainframe)
        toplvl.leftframe.pack(side=LEFT, fill="both", expand=True)
        toplvl.leftframe.place(relx=0.01, rely=0.08, relheight=0.93, relwidth=0.09)
        toplvl.leftframe.configure(relief=GROOVE)
        toplvl.leftframe.configure(background="#ffffff")
        toplvl.leftframe.configure(highlightbackground="#000000")
        toplvl.leftframe.configure(highlightcolor="black")
        
        toplvl.displayframe = Frame(toplvl.mainframe)
        toplvl.displayframe.pack(side=RIGHT, fill="both", expand=True)
        toplvl.displayframe.place(relx=0.1, rely=0.08, relheight=0.93, relwidth=0.89)
        toplvl.displayframe.configure(relief=GROOVE)
        toplvl.displayframe.configure(background="#ffffff")
        toplvl.displayframe.configure(highlightbackground="#000000")
        toplvl.displayframe.configure(highlightcolor="black")
        
        toplvl.topframe = Frame(toplvl.mainframe)
        toplvl.topframe.pack(side=LEFT, fill="both", expand=True)
        toplvl.topframe.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)
        toplvl.topframe.configure(relief=GROOVE)
        toplvl.topframe.configure(background="#ffffff")
        toplvl.topframe.configure(highlightbackground="#000000")
        toplvl.topframe.configure(highlightcolor="black")
        
#***#################### right frame separators #####################***#
        
        Rseparator6 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator6.pack(fill=X, padx=5, pady=5)
        Rseparator6.place(relx=0, rely=0.25, relwidth=1)
        
        Rseparator12 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator12.pack(fill=X, padx=5, pady=5)
        Rseparator12.place(relx=0, rely=0.5, relwidth=1)
        
        Rseparator18 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator18.pack(fill=X, padx=5, pady=5)
        Rseparator18.place(relx=0, rely=0.75, relwidth=1)
        
#***####################### top frame ############################***#
        
        topleft = Frame(toplvl.topframe)
        topleft.pack(side=RIGHT, fill="both", expand=True)
        topleft.place(relx=0, rely=0, relheight=1, relwidth=0.09)
        topleft.configure(relief=GROOVE)
        topleft.configure(background="#ffffff")
        topleft.configure(highlightbackground="#000000")
        topleft.configure(highlightcolor="black")
        topleft.configure(bd=2)
        
        topright = Frame(toplvl.topframe)
        topright.pack(side=RIGHT, fill="both", expand=True)
        topright.place(relx=0.091, rely=0, relheight=1, relwidth=0.91)
        topright.configure(relief=GROOVE)
        topright.configure(background="#ffffff")
        topright.configure(highlightbackground="#000000")
        topright.configure(highlightcolor="black")
        topright.configure(bd=2)
        
        uhrzeit = Label(topleft, text="Uhrzeit")
        uhrzeit.place(relx=.5, rely=.5, anchor="center")

        topright.grid_rowconfigure(0, weight=1)
        topright.grid_rowconfigure(1, weight=1)
        topright.grid_columnconfigure(0, weight=1)
        topright.grid_columnconfigure(6, weight=1)
        
        woche = Label(topright, text="Woche")
        woche.grid(row=0, column=3)
        
        monday = Label(topright, text="Montag")
        monday.grid(row=1, column=0)
        
        tuesday = Label(topright, text="Dienstag")
        tuesday.grid(row=1, column=1)
        
        wednesday = Label(topright, text="Mittwoch")
        wednesday.grid(row=1, column=2)
        
        thursday = Label(topright, text="Donnerstag")
        thursday.grid(row=1, column=3)
        
        friday = Label(topright, text="Freitag")
        friday.grid(row=1, column=4)
        
        saturday = Label(topright, text="Samstag")
        saturday.grid(row=1, column=5)
        
        sunday = Label(topright, text="Sonntag")
        sunday.grid(row=1, column=6)
        
#***####################### left frame ############################***#
        
        first6 = Frame(toplvl.leftframe)
        first6.pack(side=RIGHT, fill="both", expand=True)
        first6.place(relx=0, rely=0, relheight=0.25, relwidth=1)
        first6.configure(relief=GROOVE)
        first6.configure(background="#ffffff")
        first6.configure(highlightbackground="#000000")
        first6.configure(highlightcolor="black")
        first6.configure(bd=2)
        
        second6 = Frame(toplvl.leftframe)
        second6.pack(side=RIGHT, fill="both", expand=True)
        second6.place(relx=0, rely=0.25, relheight=0.25, relwidth=1)
        second6.configure(relief=GROOVE)
        second6.configure(background="#ffffff")
        second6.configure(highlightbackground="#000000")
        second6.configure(highlightcolor="black")
        second6.configure(bd=2)
        
        third6 = Frame(toplvl.leftframe)
        third6.pack(side=RIGHT, fill="both", expand=True)
        third6.place(relx=0, rely=0.50, relheight=0.25, relwidth=1)
        third6.configure(relief=GROOVE)
        third6.configure(background="#ffffff")
        third6.configure(highlightbackground="#000000")
        third6.configure(highlightcolor="black")
        third6.configure(bd=2)
        
        fourth6 = Frame(toplvl.leftframe)
        fourth6.pack(side=RIGHT, fill="both", expand=True)
        fourth6.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)
        fourth6.configure(relief=GROOVE)
        fourth6.configure(background="#ffffff")
        fourth6.configure(highlightbackground="#000000")
        fourth6.configure(highlightcolor="black")
        fourth6.configure(bd=2)
        
        cl1 = Label(first6, text="0-6")
        cl1.place(relx=.5, rely=.5, anchor="center")

        cl2 = Label(second6, text="6-12")
        cl2.place(relx=.5, rely=.5, anchor="center")
        
        cl3 = Label(third6, text="12-18")
        cl3.place(relx=.5, rely=.5, anchor="center")
        
        cl4 = Label(fourth6, text="18-24")
        cl4.place(relx=.5, rely=.5, anchor="center")
        
def display_mp():
    
    print ('...loading: display_mp')
    
    new_frame = Machine_planning()
    

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
        self.mpButt = Button(self.toolbar, text="MP", command=lambda:[display_mp()])
        self.mpButt.pack(side=LEFT, padx=2, pady=2)
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

        self.leftframe = Frame()
        
        self.topframe = Frame()
        
        

   
#def start_gui():
    #global val, w, root
root = Tk()
toplvl = Crux (root)

root.mainloop()
