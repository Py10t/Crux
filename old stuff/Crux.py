# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

import tkinter as tk
from tkinter import ttk
import stuff
import os
import basedata
import coredb
import datetime
from tkinter import filedialog


#***####################### ******* ############################***#
#***####################### CLASSES ############################***#
#***####################### ******* ############################***#


class Statusbar(tk.Label):

    def __init__(self, master):

        print ('...loading: Statusbar')

        super().__init__()

        self.status = tk.Label(master, text="Preparing to do nothing...", bd=1, relief="sunken", anchor="w")


class Navbar(tk.Frame):
    pass

    # def __init__(self, master):
    #
    #     print ('...loading: Navbar')
    #
    #     super().__init__()
    #     # self.toolbar = tk.Frame(master, bg="grey")
    #     self.insertButt = tk.Button(master, text="New(Demo)", command=lambda:[newdata()])
    #     self.insertButt.pack(side=tk.BOTTOM, padx=2, pady=2)


class Toolbar(tk.Frame):

    def __init__(self, master):

        print ('...loading: Toolbar')

        super().__init__()

        self.frame = tk.Frame(master)
        # self.insertButt = ttk.Button(self.frame, text="New(Demo)", command=lambda:[Crux.doNothing(self)])
        # self.insertButt.pack(side="left", padx=2, pady=2)
        # self.printButt = ttk.Button(self.frame, text="Search", command=lambda:[Crux.doNothing(self)])
        # self.printButt.pack(side="left", padx=2, pady=2)
        # self.stockButt = ttk.Button(self.frame, text="Stock", command=lambda:[Crux.doNothing(self)])
        # self.stockButt.pack(side="left", padx=2, pady=2)
        # self.machinesButt = ttk.Button(self.frame, text="Engines", command=lambda:[Crux.doNothing(self)])
        # self.machinesButt.pack(side="left", padx=2, pady=2)
        self.mpButt = ttk.Button(self.frame, text="MP", command=lambda:[Crux.mp_button(master)])
        self.mpButt.pack(side="left", padx=2, pady=2)
        self.auditButt = ttk.Button(self.frame, text="Audit", command=lambda:[Crux.audit_buttons(master)])
        self.auditButt.pack(side="left", padx=2, pady=2)


class Mainmenu(tk.Menu):

    def __init__(self, master):

        print ('...loading: MainMenu')

        super().__init__()

        self.menubar = tk.Menu(master)
        # self.menubar.add_command(label="Hello!", command=self.subMenu)
        # self.menubar.add_command(label="Quit!", command=root.quit)

        self.subMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="New Project ...", command=Crux.doNothing)
        self.subMenu.add_command(label="New", command=Crux.doNothing)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=root.destroy)


class Mainframe(tk.Frame):

    def __init__(self, master):

        print ('...loading: MainMenu')

        super().__init__()

        self.frame = tk.Frame(master, bg="grey")


class Machine_Planning(tk.Frame):

    def __init__(self, master):

        print('...loading: MP/__init__')

        super().__init__()

        # ***####################### Main Frames for MP ############################***#

        self.leftframe = tk.Frame(master)
        self.leftframe.pack(side="left", fill="both", expand=True)
        self.leftframe.place(relx=0.01, rely=0.08, relheight=0.91, relwidth=0.09)
        self.leftframe.configure(relief="groove")
        self.leftframe.configure(background="#ffffff")
        self.leftframe.configure(highlightbackground="#000000")
        self.leftframe.configure(highlightcolor="black")

        self.displayframe = tk.Frame(master)
        self.displayframe.pack(side="right", fill="both", expand=True)
        self.displayframe.place(relx=0.11, rely=0.08, relheight=0.91, relwidth=0.88)
        self.displayframe.configure(relief="groove")
        self.displayframe.configure(background="#ffffff")
        self.displayframe.configure(highlightbackground="#000000")
        self.displayframe.configure(highlightcolor="black")

        self.topframe = tk.Frame(master)
        self.topframe.pack(fill="both", expand=True)
        self.topframe.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)
        self.topframe.configure(relief="groove")
        self.topframe.configure(background="#ffffff")
        self.topframe.configure(highlightbackground="#000000")
        self.topframe.configure(highlightcolor="black")

        # ***####################### top frames ############################***#

        self.topleft = tk.Frame(self.topframe)
        self.topleft.pack(side="left", fill="both", expand=True)
        self.topleft.place(relx=0.001, rely=0.01, relheight=0.99, relwidth=0.092)
        self.topleft.configure(relief="groove")
        self.topleft.configure(highlightbackground="#000000")
        self.topleft.configure(highlightcolor="black")
        self.topleft.configure(bd=2)

        self.topright = tk.Frame(self.topframe)
        self.topright.pack(side="right", fill="both", expand=True)
        self.topright.place(relx=0.102, rely=0.01, relheight=0.99, relwidth=0.898)
        self.topright.configure(relief="groove")
        self.topright.configure(highlightbackground="#000000")
        self.topright.configure(highlightcolor="black")
        self.topright.configure(bd=2)

        self.left_bar()
        self.week_frame()
        self.configuring_grid()
        self.filling_grid()
        self.topleft_button()

    def left_bar(self):

        print("...loading: Machine_Planning/left_bar")

        self.machine_numbers = [
                                'Maschine 1',
                                'Maschine 2',
                                'Maschine 3',
                                'Maschine 4',
                                'Maschine 5',
                                'Maschine 6',
                                'Maschine 7',
                                'Maschine 8'
                                ]
        self.buttons =[]
        i = 0

        tk.Grid.columnconfigure(self.leftframe, 0, weight=1)

        for item in self.machine_numbers:

            self.buttons.append(tk.Button(self.leftframe, text=item, command=lambda: [self.engine_popup(self.leftframe, item)]))
            self.buttons[i].grid(row=i, column=0, sticky="nsew", rowspan=1)
            tk.Grid.rowconfigure(self.leftframe, i, weight=1)
            i = i+1

    def display_frame(self):

        print("...loading: Machine_Planning/display_frame")
        pass

    def week_frame(self):

        #grid row = 0 muss noch zwei Pfeilbutton (rechts links) und "KW XX" in der Mitte werden

        print("...loading: Machine_Planning/week_frame")

        self.week_days = [
                                'Montag',
                                'Dienstag',
                                'Mittwoch',
                                'Donnerstag',
                                'Freitag',
                                'Samstag',
                                'Sonntag'
                                ]
        self.buttons =[]
        i = 0

        tk.Grid.rowconfigure(self.topright, 0, weight=1)

        for item in self.week_days:

            self.buttons.append(tk.Button(self.topright, text=item, command=lambda: [newstockbuttons()]))
            self.buttons[i].grid(row=0, column=i, sticky="nsew", rowspan=1)
            tk.Grid.columnconfigure(self.topright, i, weight=1)
            i = i+1

    def new_entry_button(self):

        print("...loading: Machine_Planning/new_entry_button")
        pass

    def configuring_grid(self):

        print("...loading: Machine_Planning/configuring_grid")

        for i in range(8):
            tk.Grid.rowconfigure(self.displayframe, i, weight=1)
            i = i+1
            for j in range(28):
                tk.Grid.columnconfigure(self.displayframe, i, weight=1)
                j = j+1

    def filling_grid(self):

        print("...loading: Machine_Planning/filling_grid")

        titlelabel1 = tk.Label(self.displayframe, text="Artikel X", bg="grey", height=3)
        titlelabel1.grid(row=0, column=0, sticky='we', columnspan=12)

        titlelabel2 = tk.Label(self.displayframe, text="Artikel X", bg="yellow", height=3)
        titlelabel2.grid(row=1, column=0, sticky='we', columnspan=10)

        titlelabel3 = tk.Label(self.displayframe, text="Artikel X", bg="blue", height=3)
        titlelabel3.grid(row=2, column=0, sticky='we', columnspan=8)

        titlelabel4 = tk.Label(self.displayframe, text="Artikel X", bg="purple", height=3)
        titlelabel4.grid(row=3, column=0, sticky='we', columnspan=4)

        titlelabel5 = tk.Label(self.displayframe, text="Artikel X", bg="orange", height=3)
        titlelabel5.grid(row=4, column=0, sticky='we', columnspan=7)

        titlelabel6 = tk.Label(self.displayframe, text="Artikel X", bg="grey", height=3)
        titlelabel6.grid(row=5, column=0, sticky='we', columnspan=10)

        titlelabel7 = tk.Label(self.displayframe, text="Artikel X", bg="green", height=3)
        titlelabel7.grid(row=6, column=0, sticky='we', columnspan=4)

        titlelabel8 = tk.Label(self.displayframe, text="Artikel X", bg="red", height=3)
        titlelabel8.grid(row=7, column=0, sticky='we', columnspan=11)

        titlelabel9 = tk.Label(self.displayframe, text="Artikel X", bg="grey", height=3)
        titlelabel9.grid(row=3, column=4, sticky='we', columnspan=2)

    def topleft_button(self):

        print("topleft_button")

        New_Plan_Butt = ttk.Button(self.topleft, text="Neuer Plan", command=lambda: [self.new_plan_frame(self.leftframe)])
        New_Plan_Butt.pack(fill="both", expand=1)

    def engine_popup(self, master, engine_title):

        print("engine_popup")

        self.maschinen_popup = Enginedisplayer(master, engine_title)

    def new_plan_frame(self, master):

        print("new_plan_frame")

        engineframe = tk.Toplevel(master)
        engineframe.geometry("300x400")
        engineframe.title("Katze")

        label_names = ["Eintrag", "Eintrag", "Eintrag", "Eintrag", "Eintrag", "Eintrag", "Eintrag", "Eintrag" ]

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
        # entries enthält alle entry boxes des folgenden for loops
        self.entries = []

        self.optionX = 2
        optDict = {1: self.customer_parameter,
                   2: self.article_parameter,
                   3: self.material_parameter,
                   }
        self.label_choice = optDict[self.optionX]

        i=0

        for item in self.label_choice:
            nameL = tk.Label(engineframe, text=item)
            nameL.grid(row=i + 1, column=0, sticky="e")

            self.entries.append(tk.Entry(engineframe))
            self.entries[i].delete(0, tk.END)
            self.entries[i].insert(0, label_names[i])
            self.entries[i].grid(row=i + 1, column=1)

            i = i + 1

        New_Plan_Butt = ttk.Button(engineframe, text="Erstellen",
                                   command=lambda: [self.new_plan_frame(self.leftframe)])
        New_Plan_Butt.grid()


class Enginedisplayer(tk.Frame):

    def __init__(self, master, engine_title):
        engineframe = tk.Toplevel(master)
        engineframe.geometry("300x400")
        engineframe.title(engine_title)

        # Labels
        StatusL = tk.Label(engineframe, text='Engine Status : ')
        StatusL.grid(row=1, column=0, sticky="e")
        ArticleL = tk.Label(engineframe, text='Article : ')
        ArticleL.grid(row=2, column=0, sticky="e")
        StartL = tk.Label(engineframe, text='Start (d/m/y - time) : ')
        StartL.grid(row=3, column=0, sticky="e")
        EndL = tk.Label(engineframe, text='End (d/m/y - time) : ')
        EndL.grid(row=5, column=0, sticky="e")

        StatusL2 = tk.Label(engineframe, text='Online', fg="green")
        StatusL2.grid(row=1, column=1, sticky="e")
        Article2 = tk.Label(engineframe, text='3K - 380248')
        Article2.grid(row=2, column=1, sticky="e")
        StartL2 = tk.Label(engineframe, text='30.03.2018')
        StartL2.grid(row=3, column=1, sticky="e")
        StartL3 = tk.Label(engineframe, text='8:00')
        StartL3.grid(row=4, column=1, sticky="e")
        EndL2 = tk.Label(engineframe, text='05.04.2018')
        EndL2.grid(row=5, column=1, sticky="e")
        EndL2 = tk.Label(engineframe, text='18:00')
        EndL2.grid(row=6, column=1, sticky="e")

        button = tk.Button(engineframe, text="Open TD", command=lambda: [self.openfile()])
        button.grid(column=0, row=0)


#***####################### ******* ############################***#
#***#######################  Crux   ############################***#
#***####################### ******* ############################***#


class Crux(tk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        master.geometry("1000x600")
        #        master.geometry("800x600+834+103")
        master.title("Crux")
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")
        # "tearOff=False" globally removes dashed lines in the drop down
        master.option_add('*tearOff', False)


        print(str(datetime.datetime.now()))

        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.mainmenu = Mainmenu(self)
        self.mainframe = Mainframe(self)
        #
        self.statusbar.status.pack(side ='bottom', fill="x")
        self.toolbar.frame.pack(side="top", fill="x")
        # self.toolbar.pack()
        self.navbar.pack(side="top", fill="x")
        self.mainframe.frame.pack(side="top", fill="both", expand=True)
        # self.main.menu.pack(side="right", fill="both", expand=True)

        master.configure(menu=self.mainmenu.menubar)

    def doNothing(self):

        print('LuL')

# ***#######################  Audit  ############################***#

    def audit_buttons(self):

        print('...generating: auditbuttons')

        self.audit_button_1=ttk.Button(self.mainframe.frame, text="Inhaltsverzeichnis", command=lambda:[Crux.eval_link_state(self, 1)])
        self.audit_button_1.grid(row=0, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_2=ttk.Button(self.mainframe.frame, text="Firmengeschichte", command=lambda:[Crux.eval_link_state(self, 2)])
        self.audit_button_2.grid(row=1, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_3=ttk.Button(self.mainframe.frame, text="Tätigkeitsfeld", command=lambda:[Crux.eval_link_state(self, 3)])
        self.audit_button_3.grid(row=2, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_4=ttk.Button(self.mainframe.frame, text="Kunden", command=lambda: [Crux.eval_link_state(self, 4)])
        self.audit_button_4.grid(row=3, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_5=ttk.Button(self.mainframe.frame, text="Organigramm", command=lambda: [Crux.eval_link_state(self, 5)])
        self.audit_button_5.grid(row=4, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_6=ttk.Button(self.mainframe.frame, text="Prozesslandschaft", command=lambda: [Crux.eval_link_state(self, 6)])
        self.audit_button_6.grid(row=5, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_7 = ttk.Button(self.mainframe.frame, text="Zuständigkeiten", command=lambda: [Crux.eval_link_state(self, 7)])
        self.audit_button_7.grid(row=6, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_8 = ttk.Button(self.mainframe.frame, text="Korrelationsmatrix", command=lambda: [Crux.eval_link_state(self, 8)])
        self.audit_button_8.grid(row=7, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_9 = ttk.Button(self.mainframe.frame, text="Leitlinien", command=lambda: [Crux.eval_link_state(self, 9)])
        self.audit_button_9.grid(row=8, column=0, sticky="n"+ "s" + "e" + "w")

        self.audit_button_10 = ttk.Button(self.mainframe.frame, text="Kontext der Organisation", command=lambda: [Crux.eval_link_state(self, 10)])
        self.audit_button_10.grid(row=9, column=0, sticky="n"+ "s" + "e" + "w")

        self.delete_button = tk.Button(self.mainframe.frame, text="Pfad entfernen", command=lambda: [Crux.delete_path_var(self, self.tkvar.get())])
        self.delete_button.grid(row=0, column=1, sticky="n"+ "s" + "e" + "w")

        self.tkvar = tk.StringVar(self.mainframe.frame)
        choices = [self.audit_button_1.cget('text'),
                   self.audit_button_2.cget('text'),
                   self.audit_button_3.cget('text'),
                   self.audit_button_4.cget('text'),
                   self.audit_button_5.cget('text'),
                   self.audit_button_6.cget('text'),
                   self.audit_button_7.cget('text'),
                   self.audit_button_8.cget('text'),
                   self.audit_button_9.cget('text'),
                   self.audit_button_10.cget('text'),
                   ]
        self.tkvar.set('Eintrag auswählen')  # set the default option

        popupMenu = tk.OptionMenu(self.mainframe.frame, self.tkvar, *choices)
        popupMenu.grid(row=1, column=1)

    def eval_link_state(self, x):

        #evaluates if the auditbutton link to db is True or False, if False it opens askopenfile

        print('...loading: eval_link_state')

        optDict={
                1:self.audit_button_1,
                2:self.audit_button_2,
                3:self.audit_button_3,
                4:self.audit_button_4,
                5:self.audit_button_5,
                6:self.audit_button_6,
                7:self.audit_button_7,
                8:self.audit_button_8,
                9:self.audit_button_9,
                10:self.audit_button_10
                }

        result = coredb.get_path_var(x)

        if len(result) == 0:
            print("Lul")
            self.writing_link_to_db(x, optDict[x].cget('text'))

        else:
            print(result)
            os.startfile(str(result[0][0]))

    def writing_link_to_db(self, x_intID, file_name):

        print('...writing: lst to db')

        path_var = filedialog.askopenfilename()
        lst = [file_name, path_var, x_intID]
        lst.append(str(datetime.datetime.now()))
        coredb.insert_new_path(lst)

    def delete_path_var(self, file_name):

        print("...loading: delete_path_var")

        print(file_name)

        coredb.delete_dir_values(file_name)

    def mp_button(self):

        mp_frame = Machine_Planning(self.mainframe.frame)
        
        

   
#def start_gui():
if __name__ == "__main__":
    root = tk.Tk()
    Crux(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
