# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:52:49 2017

@author: Andrasz
"""
from tkinter import *
    
    
def doNothing():
    print("do nothing")
    
class Stammdaten:


    def __init__(self):
        #invoking all attr. on object
        
        self.name = 0
        
#customer
        self.address = 0
        self.email = 0 
        
#article
        self.intID = 0
        self.extID = 0
        #amount right now produced on the machine
        self.manufacturing = 0
        #tbm = to be manufactured like still waiting or left for a deadline
        self.tbm = 0
        #ppc = price per 100
        self.ppcent = 0
        #mincost = calculated minimum
        self.mincost = 0
        self.weight = 0
        #dimensions should lead to a drawing or something like that
        self.dimensions = 0
        #material should be linked to a material in db
        self.material = 0
        self.stock = 0
        
#material
        self.company = 0
        self.price = 0
        
        
class Basic_box:
    
    
    def __init__(self, x_title, x_names, x_command):
                
        x = len(x_names)
        y = "300x" + str(25+x*25)
            
        box = Toplevel()
        box.geometry(y)
        box.title("LuL")

        names = x_names

        for item in names:
            box.insertButt = Button(box, text=item)
            box.insertButt.pack()
            x = x_command[names.index(item)]
#            hier fehlt der .destroy command
            box.insertButt.config(command = x_command[names.index(item)])
            
            
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
        
        Rseparator1 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator1.pack(fill=X, padx=5, pady=5)
        Rseparator1.place(relx=0, rely=0.125, relwidth=1)
        
        Rseparator2 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator2.pack(fill=X, padx=5, pady=5)
        Rseparator2.place(relx=0, rely=0.25, relwidth=1)
        
        Rseparator3 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator3.pack(fill=X, padx=5, pady=5)
        Rseparator3.place(relx=0, rely=0.375, relwidth=1)
        
        Rseparator4 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator4.pack(fill=X, padx=5, pady=5)
        Rseparator4.place(relx=0, rely=0.5, relwidth=1)
        
        Rseparator5 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator5.pack(fill=X, padx=5, pady=5)
        Rseparator5.place(relx=0, rely=0.625, relwidth=1)
        
        Rseparator6 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator6.pack(fill=X, padx=5, pady=5)
        Rseparator6.place(relx=0, rely=0.75, relwidth=1)
        
        Rseparator7 = Frame(toplvl.displayframe, height=2, bd=1, relief=SUNKEN)
        Rseparator7.pack(fill=X, padx=5, pady=5)
        Rseparator7.place(relx=0, rely=0.875, relwidth=1)
        
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
        
        New_Plan_Butt = Button(topleft, text="Neu", command=lambda:[searchlist()])
        New_Plan_Butt.pack(fill=BOTH, expand=1)
        
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

        
        titlelabel1 = Label(toplvl.displayframe, bg ="black", height=3)
        titlelabel1.grid(row=0, column=0, sticky='we', columnspan=12)
        
        titlelabel2 = Label(toplvl.displayframe, bg ="yellow", height=3)
        titlelabel2.grid(row=1, column=0, sticky='we', columnspan=10)
        
        titlelabel3 = Label(toplvl.displayframe, bg ="blue", height=3)
        titlelabel3.grid(row=2, column=0, sticky='we', columnspan=8)
        
        titlelabel4 = Label(toplvl.displayframe, bg ="black", height=3)
        titlelabel4.grid(row=3, column=0, sticky='we', columnspan=4)
        
        titlelabel5 = Label(toplvl.displayframe, bg ="orange", height=3)
        titlelabel5.grid(row=4, column=0, sticky='we', columnspan=7)
        
        titlelabel6 = Label(toplvl.displayframe, bg ="grey", height=3)
        titlelabel6.grid(row=5, column=0, sticky='we', columnspan=10)
        
        titlelabel7 = Label(toplvl.displayframe, bg ="green", height=3)
        titlelabel7.grid(row=6, column=0, sticky='we', columnspan=4)
        
        titlelabel8 = Label(toplvl.displayframe, bg ="red", height=3)
        titlelabel8.grid(row=7, column=0, sticky='we', columnspan=11)