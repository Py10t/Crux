# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:01:12 2018

@author: andrasz
"""

import sqlite3

conn = sqlite3.connect('coredatabase.db')

c = conn.cursor()
    
#c.execute(""" CREATE TABLE coredatabase (
#            name text,
#            address text,
#            price real
#            )""")

def insert_stuff(emp):
    
    print ('...loading: insert_stuff()')
    
    with conn:
        c.execute("INSERT INTO coredatabase VALUES (:name, :address, :price)", {'name': emp.name, 'address': emp.address, 'price': emp.email})
    get_stuff_by_name('2P GmbH')
    get_everything()

       
def get_stuff_by_name(searchobject):
    
    print ('...loading: get_stuff_by_name()')
    
    c.execute("SELECT * FROM coredatabase WHERE name=:name", {'name': searchobject})
    return c.fetchall()
    

def get_everything():
    
    print ('...loading: get_everything()') 
    
    c.execute("SELECT * FROM coredatabase")
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

#def get_emps_by_name(lastname):
#    c.execute("SELECT * FROM coredatabase WHERE last=:last", {'last':lastname})
#    print (c.fetchone())

#conn.commit()
#
#conn.close()

#c.execute(""" CREATE TABLE coredatabase (
#            name text,
#            address text,
#            email text,
#            interneBez text,
#            externeBez text,
#            weight real,
#            manufacturing integer,
#            zufertigen integer,
#            ppcent real,
#            mincost real,
#            dimensions text,
#            material text,
#            stock integer,
#            company text,
#            price real
#            )""")

#    with conn:
#        c.execute("INSERT INTO coredatabase VALUES (:name, :last, :pay)", {
#                'name': emp.name, 
#                'address': emp.address,
#                'email': emp.email,
#                'interneBez': emp.interneBez,
#                'externeBez': emp.externeBez,
#                'weight': emp.weight,
#                'manufacturing': emp.manufacturing,
#                'zufertigen': emp.zufertigen,
#                'ppcent': emp.ppcent,
#                'mincost': emp.mincost,
#                'dimensions': emp.dimensions,
#                'material': emp.material,
#                'stock': emp.stock,
#                'company': emp.company,
#                'price': emp.price
#                })