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
import datetime
from tkinter import filedialog


#***####################### ******* ############################***#
#***####################### CLASSES ############################***#
#***####################### ******* ############################***#

class Modify_Object:
    
    #takes 1 list and 1 variable to indicate to which db it belongs
    
    def __init__(self, dbentry_lst, label_names, popup_choice):
        
        print ('...loading: Modify_Object')
        
        modifyframe()
        
        i = 0
        
        self.customer_parameter = [
                            'name', 
                            'address',
                            'email'
                            ]
        
        self.article_parameter = [
                            'name',
                            'extID',
                            'weight',
                            'ppcent',
                            'cavities',
                            'cycle_time',
                            'material'
                            ]
        self.material_parameter = [
                            'name',
                            'material',
                            'company',
                            'price'
                            ]
        #entries enthält alle entry boxes des folgenden for loops
        self.entries = []
        
        self.optionX = label_names
        optDict = {1 : self.customer_parameter,
                   2 : self.article_parameter,
                   3 : self.material_parameter,
                   }
        self.label_choice = optDict[self.optionX]
        
        
        for item in self.label_choice:
            nameL = Label(toplvl.leftframe, text=item)
            nameL.grid(row=i+1, column=0, sticky=E)

            self.entries.append(Entry(toplvl.leftframe))
            self.entries[i].delete(0, END)
            self.entries[i].insert(0, dbentry_lst[i])
            self.entries[i].grid(row=i+1, column=1)
            
            i = i+1
        
        self.tkvar = StringVar(toplvl.topframe)
        choices = {
                1 :'Neuer Eintrag',
                2 :'Eintrag aktualisieren', 
                3 :'Eintrag Entfernen'
                }
        self.tkvar.set(choices[popup_choice]) # set the default option
        
        popupMenu = OptionMenu(toplvl.leftframe, self.tkvar, *choices)
        popupMenu.grid()
        
        confirm_Butt = Button(toplvl.leftframe, 
                        text="Confirm", 
                        command=lambda:[self.return_function()])
        confirm_Butt.grid()
        
        
    def cleaning_entries(self, x):
        print(len(x))
        if len(x)==0:
            pass
        return x


    def update_dbframe(self):
        
        ("...loading: Modifying_Object/update_dbframe()")
        
        lst = startmodule([4, self.optionX])
        lst.append(self.optionX)
        
        displaydb(lst)
        
        
    def getem(self):
            
        ("...loading: Modifying_Object/getem()")
        
        module_choice = self.tkvar.get()
                
        optDict = {'Neuer Eintrag' : [6],
                   'Eintrag aktualisieren' : [2],
                   'Eintrag Entfernen' : [5],
                   }
        lst = optDict[module_choice]
        
        print(self.optionX)
        
        if lst == [2]:
            if self.optionX == 1:
                lst = [1]
            elif self.optionX == 2:
                lst = [2]
            elif self.optionX == 3:
                lst = [3]
            else:
                print ('FEHLER IN DER MATRIX')
                
        
        for i in range(len(self.entries)):
            lst.append(self.entries[i].get())
        
        startmodule(lst)
        
        self.update_dbframe()
        
    
    def return_function(self):
        
        lst = []
        
        for i in range(len(self.entries)):
            lst.append(self.entries[i].get())
        
        
        module_choice = self.tkvar.get()
                
        optDict = {'Neuer Eintrag' : enter_data_into_DB,
                   'Eintrag aktualisieren' : [2],
                   'Eintrag Entfernen' : [5],
                   }
        lst = optDict[module_choice](self.optionX, lst)


class Insert_new_stuff_into_DB:
    
    def __init__(self, db_var, lst):

        print('...loading: Insert_new_stuff_into_DB')
        
        current_time = datetime.datetime.now()
#        lst.append(str(current_time.strftime))
        lst.append(str(current_time))
        
        db_choice = db_var
        optDict = {1 : self.new_customer,
                   2 : self.new_article,
                   3 : self.new_material,
                   }
        optDict[db_choice](lst)
        
    def new_customer(self, lst):

        self.full_lst = [6]  # für die startmodule option
        for i in lst:
            self.full_lst.append(i)
    
    
    def new_article(self, lst):

        intID = 1
        
        self.full_lst = [7, intID] # für die startmodule option
        for i in lst:
            self.full_lst.append(i)
    
    
    def new_material(self, lst):

        self.full_lst = [8]  # für die startmodule option
        for i in lst:
            self.full_lst.append(i)


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
        
        modifyframe()
        displayframe()
        
        #Labels
        self.searchL = Label(toplvl.topframe, text='Search for: ')
        self.searchL.grid(row=1, column=0, sticky=E)
        
        #Entry boxes
        self.searchE = Entry(toplvl.topframe)
        self.searchE.delete(0, END)
        self.searchE.insert(0, "2P GmbH")
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
        
        optionX = self.tkvar2.get()
        optDict = {'Customer' : [4, 1],
                   'Article' : [4, 2],
                   'Material' : [4, 3],
                   }
        lst = startmodule(optDict[optionX])
        
        self.db_var = optDict[optionX][1]
            
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
        
        print ('...loading: Search_Frame/search_func')
        
        full_lst = db_lst
        search_lst = []
        
        for x in full_lst:
            if x[s_p] == search_word:
                search_lst.append(full_lst[i])
                i = i + 1

            elif x[s_p] != search_word:
                i = i + 1
                
        search_lst.append(self.db_var)
        displaydb(search_lst)


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
# x ist eine Liste mit x[0]=option und x[1:] was für die func gebraucht wird
#-optDict[] ruft eine der def() aus dem dict auf
#
    
    print ('...loading: startmodule()')
        
    optionX = x[0]
    optDict = {1 : coredb.update_customer,
               2 : coredb.update_article,
               3 : coredb.update_material,
               4 : coredb.get_everything,
               5 : coredb.delete_customer,
               6 : coredb.insert_newcustomer,
               7 : coredb.insert_newarticle,
               8 : coredb.insert_newmaterial
               }
    print ('...Parameter: ', x)
    return optDict[optionX](x)


def enter_data_into_DB(db_var, lst):
    
    print ('...loading: enter_data_into_DB')
    
    new_stuff = Insert_new_stuff_into_DB(db_var, lst)
    startmodule(new_stuff.full_lst)


def display_mp():
    
    print ('...loading: display_mp')
    
#    new_frame = Machine_planning()
    
def searchlist():
    
    print ('...loading: searchlist')
    
#    box = Toplevel(toplvl.mainframe)
    newboxclass = Search_Frame()
    
    
def display_engines():
    
    print ('...loading: display_machines')
    
    box = Enginedisplayer()
    
    
def doNothing():
    print(toplvl.x)
    
    
def newdata():
    
    print ('...loading: newdata() button box')
    
    w = "First box"
    x = ["Customer", "Article", "Material"]
#    y = [stuff.newcustomerbox, stuff.newarticlebox, stuff.newmaterialbox]
    empty_lst = []
    for i in range (20):
        empty_lst.append("Bitte ausfüllen")
    y=[lambda: Modify_Object(empty_lst, 1, 1), lambda: Modify_Object(empty_lst, 2, 1), lambda: Modify_Object(empty_lst, 3, 1)]
    newbox = basedata.Basic_box(w, x, y)
    
    
def newstockbuttons():
    
    print ('...loading: newstockbuttons()')
    
    w = "Second box"
    x = ["Customer", "Article", "Material"]
    y = [lambda: displayhelper([4, 1]), lambda: displayhelper([4, 2]), lambda: displayhelper([4, 3])]
    newbox = basedata.Basic_box(w, x, y)


def modifyframe():
    
    print ('...loading: modifyframe() -> clearing left frame')
    
    toplvl.leftframe = Frame(toplvl.mainframe)
    toplvl.leftframe.pack(side=LEFT, fill=Y, expand=True)
    toplvl.leftframe.place(relx=0.01, rely=0.17, relheight=0.82, relwidth=0.49)
    toplvl.leftframe.configure(relief=GROOVE)
#        toplvl.leftframe.configure(background="#000000")
    toplvl.leftframe.configure(highlightbackground="#000000")
    toplvl.leftframe.configure(highlightcolor="black")
    toplvl.leftframe.configure(bd=2)
        
        
def displayframe():
# ***** Right frame ****
    #call this function to clear right frame
    
    print ('...loading: displayframe() -> clearing right frame')
    
    toplvl.displayframe = Frame(toplvl.mainframe)
    toplvl.displayframe.pack(side=RIGHT, fill=Y, expand=True)
    toplvl.displayframe.place(relx=0.51, rely=0.01, relheight=0.98, relwidth=0.48)
    toplvl.displayframe.configure(relief=GROOVE)
#    toplvl.displayframe.configure(background="#000000")
    toplvl.displayframe.configure(highlightbackground="#000000")
    toplvl.displayframe.configure(highlightcolor="black")
    toplvl.displayframe.configure(bd=2)


def displayhelper(x):
    
    print ('...loading: displayhelper()')
    
    db_var = x[1]
    
    lst = startmodule(x)
    lst.append(x[1])
    
    displaydb(lst)


def modifying_helper(x, db_value):
    
    print ('...loading: displayhelper()')
    
    box = Modify_Object(x, db_value)


def displaydb(lst):
#iterates through a list retrieved from db and displays it in rframe
    
    print ('...loading: displaydb()')
    
    displayframe()
    
    dbdisplay = Text(toplvl.displayframe)
    
    db_value = lst.pop()
    
# every entry in the DB becomes a TUPLE (...) and all of them are packed in a LIST [...]
       
    for x in lst:
        dbdisplay.insert(END, str(x) + '\n')
    
    dbdisplay.pack()
    
    button_frame =Frame(toplvl.displayframe)
    button_frame.pack(side=BOTTOM, fill=X)
#    button_frame.place(relx=0.51, rely=0.01, relheight=0.98, relwidth=0.48)
    button_frame.configure(relief=GROOVE)
    button_frame.configure(highlightbackground="#000000")
    button_frame.configure(highlightcolor="black")
    button_frame.configure(bd=2)
    
    get_marked_entry = Button(button_frame, 
                    text="get_marked", 
                    command=lambda:[object_selection(dbdisplay.selection_get())])
    
    get_marked_entry.pack(side=LEFT, padx=2, pady=2)
    
    pass_first_entry = Button(button_frame, 
                    text="modify_first_E", 
                    command=lambda:[modifying_helper(lst[0], db_value, 2)])
    
    pass_first_entry.pack(side=LEFT, padx=2, pady=2)
    
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

        print(str(datetime.datetime.now()))
        
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
