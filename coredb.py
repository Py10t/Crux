# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:01:12 2018

@author: andrasz
"""

import sqlite3

conn = sqlite3.connect('coredatabase.db')

c = conn.cursor()

""" -we establish connection to coredatabase.db,
    -then for first time run creating a table 'coredatatbase1' with given attributes
     within coredatabase.db
    -the other functions aim at inserting new objects, updating existing ones or deleting some
"""
    

#c.execute(""" CREATE TABLE coredatabase1 (
#            type int,
#            name text,
#            address text,
#            email text,
#            intID text,
#            extID text,
#            weight real,
#            ppcent real,
#            mincost real,
#            dimensions text,
#            material text,
#            company text,
#            price real
#            )""")

#c.execute(""" CREATE TABLE dbcustomers (
#            name text,
#            address text,
#            email text
#            )""")
#
#c.execute(""" CREATE TABLE dbarticles (
#            name text,
#            intID text,
#            extID text,
#            weight real,
#            ppcent real,
#            mincost real,
#            dimensions text,
#            material text
#            )""")
#    
#c.execute(""" CREATE TABLE dbmaterials (
#            name text,
#            intID text,
#            material text,
#            company text,
#            price real
#            )""")


#def insert_newstuff(x, emp):
#    
#    print ('...loading: insert_newstuff()')
#    
#    with conn:
#       c.execute("""INSERT INTO coredatabase1 VALUES (:type, :name, :address, :email, :intID, :extID, :weight, :ppcent, :mincost, :dimensions, :material, :company, :price)""", 
#                 {
#                'type':x,
#                'name': emp.name, 
#                'address': emp.address,
#                'email': emp.email,
#                'intID': emp.intID,
#                'extID': emp.extID,
#                'weight': emp.weight,
#                'ppcent': emp.ppcent,
#                'mincost': emp.mincost,
#                'dimensions': emp.dimensions,
#                'material': emp.material,
#                'company': emp.company,
#                'price': emp.price
#                })
#    get_everything()
    

def insert_newcustomer(emp):
    
    print ('...loading: insert_newcustomer()')
    
    with conn:
       c.execute("""INSERT INTO dbcustomers VALUES (:name, :address, :email)""", 
                 {
                'name': emp.name, 
                'address': emp.address,
                'email': emp.email
                })

    
def insert_newarticle(emp):
    
    print ('...loading: insert_newarticle()')
    
    with conn:
       c.execute("""INSERT INTO dbarticles VALUES (:name, :intID, :extID, :weight, :ppcent, :mincost, :dimensions, :material)""", 
                 {
                'name': emp.name, 
                'intID': emp.intID,
                'extID': emp.extID,
                'weight': emp.weight,
                'ppcent': emp.ppcent,
                'mincost': emp.mincost,
                'dimensions': emp.dimensions,
                'material': emp.material
                })

    
def insert_newmaterial(emp):
    
    print ('...loading: insert_newstuff()')
    
    with conn:
       c.execute("""INSERT INTO dbmaterials VALUES (:name, :address, :email, :intID, :extID, :weight, :ppcent, :mincost, :dimensions, :material, :company, :price)""", 
                 {
                'name': emp.name,
                'intID': emp.intID,
                'material': emp.material,
                'company': emp.company,
                'price': emp.price
                })    
       
#def get_stuff_by_type(searchobject):
#    
#    print ('...loading: get_stuff_by_type()')
#    
#    c.execute("SELECT * FROM coredatabase1 WHERE type=:type", {'type': searchobject})
#    return c.fetchall()

    
def get_stuff_by_type(x, searchobject):
    
    print ('...loading: get_stuff_by_type()')
    optDict = {1 : 'dbcustomers',
               2 : 'dbarticles',
               3 : 'dbmaterials',
               }
    dbname = optDict[x]
    c.execute("SELECT * FROM dbcustomers WHERE name=:name", {'name': searchobject})
    return c.fetchall()

       
#def get_stuff_by_name(searchobject):
#    
#    print ('...loading: get_stuff_by_name()')
#    
#    c.execute("SELECT * FROM coredatabase1 WHERE name=:name", {'name': searchobject})
#    return c.fetchall()
    

def get_everything():
    
    print ('...loading: get_everything()') 
    
    c.execute("SELECT * FROM coredatabase1")
    print (c.fetchall())


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from emplyoees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

def closedb():
    conn.close()
    
