# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:50:14 2017

@author: Andrasz
"""

from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import figure
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import csv


def initialize123():
# Importing the dataset
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

# Predicting the Test set results
        
    y_pred = regressor.predict(X_test)
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Test set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    fig1 = plt.gcf()
    plt.savefig('demplots.png')
    plt.close()
    toplvl.photo=PhotoImage(file='demplots.png')      
    toplvl.Label3 = Label(toplvl.rframe, image=toplvl.photo)
    toplvl.Label3.pack()

def doNothing():
    print(toplvl.x)
    
    
def showcsv():
    with open("Salary_Data.csv", newline = "") as file:
        reader = csv.reader(file)

   # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
         # i've added some styling
                label = tkinter.Label(toplvl.mainframe, width = 12, height = 2, \
                               text = row, relief = tkinter.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1



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
        self.subMenu.add_command(label="New", command=initialize123)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=master.destroy)

        #  "Edit"
        #self.menu.add_cascade(label="Edit", menu=self.subMenu)
        #self.editMenu.add_command(label="Redo", command=doNothing)


# ***** Toolbar *****


        self.toolbar = Frame(master, bg="grey")
        self.insertButt = Button(self.toolbar, text="Insert Image", command=doNothing)
        self.insertButt.pack(side=LEFT, padx=2, pady=2)
        self.printButt = Button(self.toolbar, text="Print", command=showcsv)
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
