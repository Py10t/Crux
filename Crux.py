# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

from tkinter import *
import stuff


def newdata():
    
    print ('...loading: newdata())') 
    
    box = Tk()
    box.geometry("300x100")

# Button for new customers
    box.insertButt = Button(box, text="Customer")
    box.insertButt.pack()
    box.insertButt.config(command=lambda: [stuff.newcustomer(), box.destroy()])
    
# Button for new articles    
    box.insertButt2 = Button(box, text="Article")
    box.insertButt2.pack()
    box.insertButt2.config(command=lambda: [doSomething(), box.destroy()])
    
def doNothing():
    print(toplvl.x)
    

def doSomething():
    
    print ('...loading: doSomething()') 
        
# Button for new customers
    newcustomerButton = Button(toplvl.rframe, text="New Customer")
    newcustomerButton.pack()
    newcustomerButton.config(command=lambda: [stuff.newcustomer(), toplvl.rframe.destroy()])
    
# Button for loading customers
    toplvl.rframe.insertButt = Button(toplvl.rframe, text="Show Customers")
    toplvl.rframe.insertButt.pack()
    toplvl.rframe.insertButt.config(command=lambda: [showdb()])
    
def showdb():
    
    print ('...loading: showdb()') 

    lst = stuff.startmodule([1])    
    dbentry = Text(toplvl.rframe)
    for x in lst:
        dbentry.insert(END, str(x) + '\n')
    dbentry.pack()
    

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
        self.insertButt = Button(self.toolbar, text="New(Demo)", command=newdata)
        self.insertButt.pack(side=LEFT, padx=2, pady=2)
        self.printButt = Button(self.toolbar, text="Print", command= lambda: [stuff.startmodule([1])])
        self.printButt.pack(side=LEFT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X)


# ***** Statusbar *****


        self.status = Label(master, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

        
# ***** Mainframe *****
        
        
        self.mainframe = Frame(master)
        self.mainframe.configure(background="#d9d9d9")
        self.mainframe.pack(side=TOP, fill=BOTH, expand=True)
        
        
# ***** Right frame ****
        
        
        self.rframe = Frame(self.mainframe)
        self.rframe.pack(fill=Y, expand=True)
        self.rframe.place(relx=0.47, rely=0.01, relheight=0.98, relwidth=0.53)
        self.rframe.configure(relief=GROOVE)
        self.rframe.configure(background="#000000")
        self.rframe.configure(highlightbackground="#000000")
        self.rframe.configure(highlightcolor="black")
        


        

    

    
    
#def start_gui():
    #global val, w, root
root = Tk()
toplvl = Crux (root)

root.mainloop()
