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
        
#***####################### Main Frames for MP ############################***#
        
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
        toplvl.topframe.pack(fill="both", expand=True)
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
        
#***####################### top frames ############################***#
        
        topleft = Frame(toplvl.topframe)
        topleft.pack(side=RIGHT, fill="both", expand=True)
        topleft.place(relx=0, rely=0, relheight=1, relwidth=0.09)
        topleft.configure(relief=GROOVE)
        topleft.configure(highlightbackground="#000000")
        topleft.configure(highlightcolor="black")
        topleft.configure(bd=2)
        
        topright = Frame(toplvl.topframe)
        topright.pack(side=RIGHT, fill="both", expand=True)
        topright.place(relx=0.091, rely=0, relheight=1, relwidth=0.91)
        topright.configure(relief=GROOVE)
        topright.configure(highlightbackground="#000000")
        topright.configure(highlightcolor="black")
        topright.configure(bd=2)
        
#***####################### top texts ############################***#
        
        canvasWeek = Canvas(topright, width= 60, height=14)
        canvasWeek.grid(row=0, column=3)
        canvasWeek.create_text(2,1, text="Woche", anchor=NW)
        
        canvasMon = Canvas(topright, width= 60, height=14)
        canvasMon.grid(row=1, column=0)
        canvasMon.create_text(2,1, text="Montag", anchor=NW)
        
        canvasTue = Canvas(topright, width= 60, height=14)
        canvasTue.grid(row=1, column=1)
        canvasTue.create_text(2,1, text="Dienstag", anchor=NW)
        
        canvasWed = Canvas(topright, width= 60, height=14)
        canvasWed.grid(row=1, column=2)
        canvasWed.create_text(2,1, text="Mittwoch", anchor=NW)
        
        canvasThur = Canvas(topright, width= 60, height=14)
        canvasThur.grid(row=1, column=3)
        canvasThur.create_text(2,1, text="Donnerstag", anchor=NW)
        
        canvasFri = Canvas(topright, width= 60, height=14)
        canvasFri.grid(row=1, column=4)
        canvasFri.create_text(2,1, text="Freitag", anchor=NW)
        
        canvasSat = Canvas(topright, width= 60, height=14)
        canvasSat.grid(row=1, column=5)
        canvasSat.create_text(2,1, text="Samstag", anchor=NW)
        
        canvasSun = Canvas(topright, width= 60, height=14)
        canvasSun.grid(row=1, column=6)
        canvasSun.create_text(2,1, text="Sonntag", anchor=NW)
        
        canvasClock = Canvas(topleft, width= 36, height=14)
        canvasClock.place(relx=.5, rely=.5, anchor="center")
        canvasClock.create_text(2,1, text="Uhrzeit", anchor=NW)
        
        topright.grid_rowconfigure(0, weight=1)
        topright.grid_rowconfigure(1, weight=1)
        topright.grid_columnconfigure(0, weight=1)
        topright.grid_columnconfigure(1, weight=1)
        topright.grid_columnconfigure(2, weight=1)
        topright.grid_columnconfigure(3, weight=1)
        topright.grid_columnconfigure(4, weight=1)
        topright.grid_columnconfigure(5, weight=1)
        topright.grid_columnconfigure(6, weight=1)
        
#***####################### left frames ############################***#
        
        M_1 = Frame(toplvl.leftframe)
        M_1.pack(side=RIGHT, fill="both", expand=True)
        M_1.place(relx=0, rely=0, relheight=0.125, relwidth=1)
        M_1.configure(relief=GROOVE)
        M_1.configure(highlightbackground="#000000")
        M_1.configure(highlightcolor="black")
        M_1.configure(bd=2)
        
        M_2 = Frame(toplvl.leftframe)
        M_2.pack(side=RIGHT, fill="both", expand=True)
        M_2.place(relx=0, rely=0.125, relheight=0.125, relwidth=1)
        M_2.configure(relief=GROOVE)
        M_2.configure(highlightbackground="#000000")
        M_2.configure(highlightcolor="black")
        M_2.configure(bd=2)
        
        M_3 = Frame(toplvl.leftframe)
        M_3.pack(side=RIGHT, fill="both", expand=True)
        M_3.place(relx=0, rely=0.25, relheight=0.125, relwidth=1)
        M_3.configure(relief=GROOVE)
        M_3.configure(highlightbackground="#000000")
        M_3.configure(highlightcolor="black")
        M_3.configure(bd=2)
        
        M_4 = Frame(toplvl.leftframe)
        M_4.pack(side=RIGHT, fill="both", expand=True)
        M_4.place(relx=0, rely=0.375, relheight=0.125, relwidth=1)
        M_4.configure(relief=GROOVE)
        M_4.configure(highlightbackground="#000000")
        M_4.configure(highlightcolor="black")
        M_4.configure(bd=2)
        
        M_5 = Frame(toplvl.leftframe)
        M_5.pack(side=RIGHT, fill="both", expand=True)
        M_5.place(relx=0, rely=0.5, relheight=0.125, relwidth=1)
        M_5.configure(relief=GROOVE)
        M_5.configure(highlightbackground="#000000")
        M_5.configure(highlightcolor="black")
        M_5.configure(bd=2)
        
        M_6 = Frame(toplvl.leftframe)
        M_6.pack(side=RIGHT, fill="both", expand=True)
        M_6.place(relx=0, rely=0.625, relheight=0.125, relwidth=1)
        M_6.configure(relief=GROOVE)
        M_6.configure(highlightbackground="#000000")
        M_6.configure(highlightcolor="black")
        M_6.configure(bd=2)
        
        M_7 = Frame(toplvl.leftframe)
        M_7.pack(side=RIGHT, fill="both", expand=True)
        M_7.place(relx=0, rely=0.75, relheight=0.125, relwidth=1)
        M_7.configure(relief=GROOVE)
        M_7.configure(highlightbackground="#000000")
        M_7.configure(highlightcolor="black")
        M_7.configure(bd=2)
        
        M_8 = Frame(toplvl.leftframe)
        M_8.pack(side=RIGHT, fill="both", expand=True)
        M_8.place(relx=0, rely=0.875, relheight=0.125, relwidth=1)
        M_8.configure(relief=GROOVE)
        M_8.configure(highlightbackground="#000000")
        M_8.configure(highlightcolor="black")
        M_8.configure(bd=2)
        
        
#***####################### left texts ############################***#
        
        M_1_Butt = Button(M_1, text="Maschine 1", command=lambda:[newstockbuttons()])
        M_1_Butt.pack(fill=BOTH, expand=1)
        
        M_2_Butt = Button(M_2, text="Maschine 2", command=lambda:[newstockbuttons()])
        M_2_Butt.pack(fill=BOTH, expand=1)
        
        M_3_Butt = Button(M_3, text="Maschine 3", command=lambda:[newstockbuttons()])
        M_3_Butt.pack(fill=BOTH, expand=1)
        
        M_4_Butt = Button(M_4, text="Maschine 4", command=lambda:[newstockbuttons()])
        M_4_Butt.pack(fill=BOTH, expand=1)
        
        M_5_Butt = Button(M_5, text="Maschine 5", command=lambda:[newstockbuttons()])
        M_5_Butt.pack(fill=BOTH, expand=1)
        
        M_6_Butt = Button(M_6, text="Maschine 6", command=lambda:[newstockbuttons()])
        M_6_Butt.pack(fill=BOTH, expand=1)
        
        M_7_Butt = Button(M_7, text="Maschine 7", command=lambda:[newstockbuttons()])
        M_7_Butt.pack(fill=BOTH, expand=1)
        
        M_8_Butt = Button(M_8, text="Maschine 8", command=lambda:[newstockbuttons()])
        M_8_Butt.pack(fill=BOTH, expand=1)
        
#***####################### !grid ############################***#
        
        toplvl.displayframe.grid_rowconfigure(0, weight=1)
        toplvl.displayframe.grid_rowconfigure(1, weight=1)
        toplvl.displayframe.grid_rowconfigure(2, weight=1)
        toplvl.displayframe.grid_rowconfigure(3, weight=1)
        toplvl.displayframe.grid_rowconfigure(4, weight=1)
        toplvl.displayframe.grid_rowconfigure(5, weight=1)
        toplvl.displayframe.grid_rowconfigure(6, weight=1)
        toplvl.displayframe.grid_rowconfigure(7, weight=1)
        
        toplvl.displayframe.grid_columnconfigure(0, weight=1)
        toplvl.displayframe.grid_columnconfigure(1, weight=1)
        toplvl.displayframe.grid_columnconfigure(2, weight=1)
        toplvl.displayframe.grid_columnconfigure(3, weight=1)
        toplvl.displayframe.grid_columnconfigure(4, weight=1)
        toplvl.displayframe.grid_columnconfigure(5, weight=1)
        toplvl.displayframe.grid_columnconfigure(6, weight=1)
        toplvl.displayframe.grid_columnconfigure(7, weight=1)
        toplvl.displayframe.grid_columnconfigure(8, weight=1)
        toplvl.displayframe.grid_columnconfigure(9, weight=1)
        toplvl.displayframe.grid_columnconfigure(10, weight=1)
        toplvl.displayframe.grid_columnconfigure(11, weight=1)

        
        titlelabel1 = Label(toplvl.displayframe, bg ="black")
        titlelabel1.grid(row=0, column=0, sticky='we', columnspan=12)
        
        titlelabel2 = Label(toplvl.displayframe, bg ="yellow")
        titlelabel2.grid(row=1, column=0, sticky='we', columnspan=10)
        
        titlelabel3 = Label(toplvl.displayframe, bg ="blue")
        titlelabel3.grid(row=2, column=0, sticky='we', columnspan=8)
        
        titlelabel4 = Label(toplvl.displayframe, bg ="black")
        titlelabel4.grid(row=3, column=0, sticky='we', columnspan=4)
        
        titlelabel5 = Label(toplvl.displayframe, bg ="orange")
        titlelabel5.grid(row=4, column=0, sticky='we', columnspan=7)
        
        titlelabel6 = Label(toplvl.displayframe, bg ="grey")
        titlelabel6.grid(row=5, column=0, sticky='we', columnspan=10)
        
        titlelabel7 = Label(toplvl.displayframe, bg ="green")
        titlelabel7.grid(row=6, column=0, sticky='we', columnspan=4)
        
        titlelabel8 = Label(toplvl.displayframe, bg ="red")
        titlelabel8.grid(row=7, column=0, sticky='we', columnspan=11)

        
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
