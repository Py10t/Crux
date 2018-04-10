# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

from tkinter import *
import stuff
import os
import basedata
import coredb
from tkinter import filedialog


#***####################### ******* ############################***#
#***####################### CLASSES ############################***#
#***####################### ******* ############################***#


class Modify_Object:
    
    def __init__(self, dbentry_lst, label_names):
        
        print (label_names)
        
        toplvl.leftframe = Frame(toplvl.mainframe)
        toplvl.leftframe.pack(side=LEFT, fill=Y, expand=True)
        toplvl.leftframe.place(relx=0.01, rely=0.17, relheight=0.83, relwidth=0.49)
        toplvl.leftframe.configure(relief=GROOVE)
#        toplvl.leftframe.configure(background="#000000")
        toplvl.leftframe.configure(highlightbackground="#000000")
        toplvl.leftframe.configure(highlightcolor="black")
        toplvl.leftframe.configure(bd=2)
        
        i = 0
        
        self.customer_parameter = [
                            'name', 
                            'address',
                            'email'
                            ]
        
        self.article_parameter = [
                            'name',
                            'intID',
                            'extID',
                            'weight',
                            'ppcent',
                            'mincost',
                            'dimensions',
                            'material'
                            ]
        self.material_parameter = [
                            'name',
                            'intID',
                            'material',
                            'company',
                            'price'
                            ]
        #entries enthält alle entry boxes des folgenden for loops
        self.entries = []
        
        optionX = label_names
        optDict = {1 : self.customer_parameter,
                   2 : self.article_parameter,
                   3 : self.material_parameter,
                   }
        choices = optDict[optionX]
        
        
        for item in choices:
            nameL = Label(toplvl.leftframe, text=item)
            nameL.grid(row=i+1, column=0, sticky=E)

            self.entries.append(Entry(toplvl.leftframe))
            self.entries[i].delete(0, END)
            self.entries[i].insert(0, dbentry_lst[i])
            self.entries[i].grid(row=i+1, column=1)
            
            i = i+1
        
        confirm_Butt = Button(toplvl.leftframe, 
                        text="Confirm", 
                        command=lambda:[self.getem()])
        confirm_Butt.grid()
        
    
    def update_dbframe(self):
        
        ("...loading: Modifying_Object/update_dbframe()")
        
        lst = coredb.get_everything([0,2])
        
        displaydb(lst)
        
        
    def getem(self):
            
        ("...loading: Modifying_Object/getem()")
        
        lst =[1]
        
        for i in range(len(self.entries)):
            lst.append(self.entries[i].get())
        
        startmodule(lst)
        
        self.update_dbframe()


class Display_Object:
    
    def __init__(self, lst):
        
        toplvl.displayframe = Frame(toplvl.mainframe)
        toplvl.displayframe.pack(side=RIGHT, fill=Y, expand=True)
        toplvl.displayframe.place(relx=0.51, rely=0.01, relheight=0.98, relwidth=0.49)
        toplvl.displayframe.configure(relief=GROOVE)
        toplvl.displayframe.configure(background="#000000")
        toplvl.displayframe.configure(highlightbackground="#000000")
        toplvl.displayframe.configure(highlightcolor="black")
        toplvl.displayframe.configure(bd=2)
        
        lst_length = len(lst[0])
        i = 0
        
        while i in range(lst_length):
            table_frame = Frame(toplvl.displayframe)
            table_frame.pack(side=LEFT, fill = Y, expand=True)
            table_frame.configure(background="red")
            table_button = Button(table_frame, text=i)
            table_button.pack()
            i = i+1


class Search_Frame:
    
    def __init__(self):
        
        print ('...loading: new search box')
        
        self.x=[]
        
        toplvl.topframe = Frame(toplvl.mainframe)
        toplvl.topframe.pack(side=LEFT, fill=Y, expand=True)
        toplvl.topframe.place(relx=0.01, rely=0.01, relheight=0.16, relwidth=0.49)
        toplvl.topframe.configure(relief=GROOVE)
        toplvl.topframe.configure(highlightbackground="#000000")
        toplvl.topframe.configure(highlightcolor="black")
        toplvl.topframe.configure(bd=2)
        
        displayframe()
        
        #Labels
        self.searchL = Label(toplvl.topframe, text='Search for: ')
        self.searchL.grid(row=1, column=0, sticky=E)
        
        #Entry boxes
        self.searchE = Entry(toplvl.topframe)
        self.searchE.delete(0, END)
        self.searchE.insert(0, "Stopfen")
        self.searchE.grid(row=2, column=1)
        
        self.tkvar = StringVar(toplvl.topframe)
        choices = ['Name', 
                'Adresse',
                'Email',
                'intID',
                'extID',
                'Gewicht',
                'Preis(%)',
                'Maße',
                'Material',
                'Hersteller',
                'Preis']
        self.tkvar.set('Such Parameter') # set the default option
        
        self.tkvar2 = StringVar(toplvl.topframe)
        choices2 = ['Customer', 
                'Article',
                'Material']
        self.tkvar2.set('Wähle DB') # set the default option
        
        popupMenu = OptionMenu(toplvl.topframe, self.tkvar, *choices)
        popupMenu.grid(row = 2, column = 2)
        
        popupMenu2 = OptionMenu(toplvl.topframe, self.tkvar2, *choices2)
        popupMenu2.grid(row = 2, column = 3)
        
        #Search Button
        searchButt = Button(toplvl.topframe, text="Search")
        searchButt.grid(row=4, column=0)
        searchButt.config(command = lambda: [self.search_helper(self.searchE.get())])
        
        
    def search_helper(self, search_word):
        
        ('... loading: search_helper')
        
#        print (self.tkvar2.get())
        
        optionX = self.tkvar2.get()
        optDict = {'Customer' : coredb.get_all_customers,
                   'Article' : coredb.get_all_articles,
                   'Material' : coredb.get_all_materials,
                   }
        lst = optDict[optionX]()
            
        self.search_func(search_word, self.tkvar.get(), lst)
        
    def search_func(self, search_word, search_parameter, db_lst,):
        
        ('... loading: search_func')
        
        i=0
        
        optDict = {'Name' : 0, 
                'Adresse' : 1,
                'Email' : 2,
                'intID' : 1,
                'extID' : 2,
                'Gewicht' : 3,
                'Preis(%)' : 4,
                'Maße' : 6,
                'Material' : 7,
                'Hersteller' : 1,
                'Preis' : 2
                }
        s_p = optDict[search_parameter]
        
        print ('...loading: C-Checkbox/search_func')
        
        full_lst = db_lst
        search_lst = []
        
        for x in full_lst:
            if x[s_p] == search_word:
                search_lst.append(full_lst[i])
                i = i + 1

            elif x[s_p] != search_word:
                i = i + 1
        
        displaydb(search_lst)


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
        self.searchE.insert(0, "Stopfen")
        self.searchE.grid(row=2, column=1)
        
        self.tkvar = StringVar(master)
        # Dictionary with options
        choices = ['Name', 
                'Adresse',
                'Email',
                'intID',
                'extID',
                'Gewicht',
                'Preis(%)',
                'Maße',
                'Material',
                'Hersteller',
                'Preis']
        
        self.tkvar.set('Such Parameter') # set the default option
        
        popupMenu = OptionMenu(master, self.tkvar, *choices)
        popupMenu.grid(row = 2, column = 2)
        
        #Checkbuttons
        self.checkVar1 = IntVar(master)
        checkbuttonC = Checkbutton(master, text = "Customers", variable = self.checkVar1)
        checkbuttonC.grid(row=3, column=1,)
#        checkbuttonC.select()
        
        self.checkVar2 = IntVar(master)
        checkbuttonA = Checkbutton(master, text = "Articles", variable = self.checkVar2)
        checkbuttonA.grid(row=3, column=2,)
#        checkbuttonA.select()
        
        self.checkVar3 = IntVar(master)
        checkbuttonM = Checkbutton(master, text = "Materials", variable = self.checkVar3)
        checkbuttonM.grid(row=3, column=3,)
#        checkbuttonM.select()
        
        #Search Button
        searchButt = Button(master, text="Confirm")
        searchButt.grid(row=4, column=0)
        searchButt.config(command = lambda: [self.search_helper(self.searchE.get())])
        
        
    def search_helper(self, search_word):
        lst = []
        if self.checkVar1.get() == True:
            lst = coredb.get_all_customers()
        elif self.checkVar2.get() == True:
            lst = coredb.get_all_articles()
        elif self.checkVar3.get() == True:
            lst = coredb.get_all_materials()
            
        self.search_func(search_word, self.tkvar.get(), lst)
        
    def search_func(self, search_word, search_parameter, db_lst,):
        
        ('... loading: search_func')
        
        print (db_lst)
        
        i=0
        
        optDict = {'Name' : 0, 
                'Adresse' : 1,
                'Email' : 2,
                'intID' : 1,
                'extID' : 2,
                'Gewicht' : 3,
                'Preis(%)' : 4,
                'Maße' : 6,
                'Material' : 7,
                'Hersteller' : 1,
                'Preis' : 2
                }
        s_p = optDict[search_parameter]
        
        print ('...loading: C-Checkbox/search_func')
        
        full_lst = db_lst
        search_lst = []
        
        for x in full_lst:
            if x[s_p] == search_word:
                search_lst.append(full_lst[i])
                i = i + 1
#                print ("if " + str(i))

            elif x[s_p] != search_word:
                i = i + 1
#                print ("else " + str(i))
        
#        print (search_lst)
#        print (len(search_lst))
        
        displaydb(search_lst)


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


#***####################### ********* ############################***#
#***####################### FUNCTIONS ############################***#
#***####################### ********* ############################***#
def startmodule(x):
    
#
#-optDict[] ruft eine der def() aus dem dict auf
#
    
    print ('...loading: startmodule()')
        
    optionX = x[0]
    optDict = {1 : coredb.update_article,
               2 : coredb.update_customer,
               3 : coredb.update_material,
               }
    print ('...Parameter: ', x)
    return optDict[optionX](x)


def display_mp():
    
    print ('...loading: display_mp')
    
    new_frame = Machine_planning()
    
def searchlist():
    
    print ('...loading: searchlist')
    
#    box = Toplevel(toplvl.mainframe)
    newboxclass = Search_Frame()
    
    db_var = newboxclass.tkvar2.get()
    
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
    y = [lambda: displayhelper([2, 1]), lambda: displayhelper([2, 2]), lambda: displayhelper([2, 3])]
    newbox = basedata.Basic_box(w, x, y)


def displayframe():
# ***** Right frame ****
    #call this function to clear right frame
    
    print ('...loading: displayframe() -> clearing right frame')
    
    toplvl.displayframe = Frame(toplvl.mainframe)
    toplvl.displayframe.pack(side=RIGHT, fill=Y, expand=True)
    toplvl.displayframe.place(relx=0.51, rely=0.01, relheight=0.98, relwidth=0.48)
    toplvl.displayframe.configure(relief=GROOVE)
    toplvl.displayframe.configure(background="#000000")
    toplvl.displayframe.configure(highlightbackground="#000000")
    toplvl.displayframe.configure(highlightcolor="black")
    toplvl.displayframe.configure(bd=2)


def displayhelper(x):
    
    print ('...loading: displayhelper()')
    
    lst = startmodule(x)
    
    displaydb(lst)


def modifying_helper(x):
    
    print ('...loading: displayhelper()')
    
    
#    optionX = searchlist.newboxclass.tkvar2.get()
#    optDict = {'Customer' : 1,
#               'Article' : 2,
#               'Material' : 3,
#               }
#    db_var = optDict[optionX]
    
    box = Modify_Object(x, 2)


def displaydb(lst):
#iterates through a list retrieved from db and displays it in rframe
    
    print ('...loading: displaydb()')
        
    displayframe()
    
    dbdisplay = Text(toplvl.displayframe)
    
    name_frame = Frame(toplvl.displayframe)
    
# every entry in the DB becomes a list and is packed in a list -> listception
    
#***####################### need a function that  ############################***#
    
#***####################### searches throught lists ############################***#
       
    for x in lst:
        dbdisplay.insert(END, str(x) + '\n')
    
    dbdisplay.pack()
    
    update = Button(toplvl.displayframe, 
                    text="get_marked", 
                    command=lambda:[object_selection(dbdisplay.selection_get())])
    
    update.pack(side=LEFT, padx=2, pady=2)
    
    update2 = Button(toplvl.displayframe, 
                    text="modify_first_E", 
                    command=lambda:[modifying_helper(lst[0])])
    
    update2.pack(side=LEFT, padx=2, pady=2)
    
    print ('db listed in rframe')
    
    
def object_selection(x):
    print (x)
    
    box = Display_Object(x)
    
    


class Crux:
    
    def __init__(self, master):
# ***** Main Menu *****
        
        master.geometry("1000x600")
#        master.geometry("800x600+834+103")
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
        self.printButt = Button(self.toolbar, text="Search", command=lambda:[searchlist()])
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
