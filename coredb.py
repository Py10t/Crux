# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:01:12 2018

@author: andrasz
"""

import sqlite3

conn = sqlite3.connect('coredatabase.db')

c = conn.cursor()

#def closedb():
#    conn.close()

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

#c.execute(""" CREATE TABLE utility_values (
#            db_name text,
#            last_intID text
#            )""")

#c.execute(""" CREATE TABLE dbcustomers (
#            intID text,
#            name text,
#            address text,
#            email text,
#            time date
#            )""")
#
#c.execute(""" CREATE TABLE dbarticles (
#            name text,
#            intID text,
#            extID text,
#            weight real,
#            ppcent real,
#            cavities int,
#            cycle_time int,
#            material text,
#            time date
#            )""")
#    
#c.execute(""" CREATE TABLE dbmaterials (
#            name text,
#            intID text,
#            material text,
#            company text,
#            price real,
#            time date
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
    

#***####################### ******* ############################***#
#***####################### INSERT #############################***#
#***####################### ******* ############################***#

def insert_newcustomer(emp):
    
    print ('...loading: insert_newcustomer()')
    
    with conn:
       c.execute("""INSERT INTO dbcustomers VALUES (:name, :address, :email)""", 
                 {
                'name': emp.name, 
                'address': emp.address,
                'email': emp.email
                })

def insert_newarticle(lst):
    
    print ('...loading: insert_newarticle()')
    
    with conn:
       c.execute("""INSERT INTO dbarticles VALUES (:name, :intID, :extID, :weight, :ppcent, :cavities, :cycle_time, :material, :time)""", 
                 {
                'intID': lst[1],
                'name': lst[2],
                'extID': lst[3],
                'weight': lst[4],
                'ppcent': lst[5],
                'cavities': lst[6],
                'cycle_time': lst[7],
                'material': lst[8],
                'time': lst[9]
                })
    
    print ("Finished inserting new article -> %s" %lst[1])
    
def insert_newmaterial(emp):
    
    print ('...loading: insert_newstuff()')
    
    with conn:
       c.execute("""INSERT INTO dbmaterials VALUES (:name, :intID, :material, :company, :price)""", 
                 {
                'name': lst[1],
                'intID': lst[1],
                'material': lst[1],
                'company': lst[1],
                'price': lst[1]
                })

#    customer = [1,2,3]
#    articles = [1,4,5,6,7,10]
#    material = [1,10,11,12]

#***####################### ******* ############################***#
#***####################### READ Table #########################***#
#***####################### ******* ############################***#
    
    
#def get_stuff_by_type(x):
#    
#    print ('...loading: get_stuff_by_type()')
#    
#    print (x)
#    displayed = []    
#    if x[0] == 1:
#        print ('x[0]=1')
#        c.execute("SELECT * FROM dbcustomers WHERE name=:name", {'name': x[1]})
#        displayed = c.fetchall()
#    elif x[0] == 2:
#        print ('x[0]=2')
#        c.execute("SELECT * FROM dbarticles WHERE name=:name", {'name': x[1]})
#        displayed = c.fetchall()
#    elif x[0] == 3:
#        print ('x[0]=3')
#        c.execute("SELECT * FROM dbmaterials WHERE name=:name", {'name': x[1]})
#        displayed = c.fetchall()
#        
#    return displayed
#       
    
#***###################################################***#
def get_everything(x):
    optionX = x[1]
    optDict = {1 : get_all_customers,
               2 : get_all_articles,
               3 : get_all_materials,
               }
    return optDict[optionX]()

def get_all_customers():
    
    print ('...loading: get_all_customers()') 
    
    c.execute("SELECT * FROM dbcustomers")
    return (c.fetchall())

def get_all_articles():
    
    print ('...loading: get_all_articles()') 
    
    c.execute("SELECT * FROM dbarticles")
    return (c.fetchall())

def get_all_materials():
    
    print ('...loading: get_all_materials()') 
    c.execute("SELECT * FROM dbmaterials")
    return (c.fetchall())

#***####################### ******* ############################***#
#***####################### UPDATE  ############################***#
#***####################### ******* ############################***#
    
def update_article(lst):
    
#    with conn:
#        c.execute("""UPDATE employees SET pay = :pay
#                    WHERE first = :first AND last = :last""",
#                  {'first': emp.first, 'last': emp.last, 'pay': pay})
    
    with conn:
        c.execute("""UPDATE dbarticles SET name = :name,
                                          intID = :intID,
                                          extID = :extID,
                                          weight = :weight,
                                          ppcent = :ppcent,
                                          mincost = :mincost,
                                          dimensions = :dimensions,
                                          material = :material
                    WHERE intID = :intID""", 
                 {
                'name': lst[1], 
                'intID': lst[2],
                'extID': lst[3],
                'weight': lst[4],
                'ppcent': lst[5],
                'mincost': lst[6],
                'dimensions': lst[7],
                'material': lst[8]
                })
        
        print ("Finished updating article %s" %lst[1])
        
def update_customer(lst):
    
    print ('...loading: update_customer()')
    
    with conn:
        c.execute("""UPDATE dbcustomers SET name = :name,
                                         address = :address,
                                         email = :email
                    WHERE name = :name""", 
                 {
                'name': lst[1], 
                'address': lst[2],
                'email': lst[3]
                })
        
        print ("Finished updating customer %s" %lst[1])
        
def update_material(lst):
    
    print ('...loading: update_material()')
    
    with conn:
        c.execute("""UPDATE dbmaterials SET name = :name,
                                          intID = :intID,
                                          material = :material,
                                          company = :company,
                                          price = :price
                    WHERE intID = :intID""", 
                 {
                'name': lst[1],
                'intID': lst[2],
                'material': lst[3],
                'company': lst[4],
                'price': lst[5]
                })
        
        print ("Finished updating material %s" %lst[1])
        
#***####################### ******* ############################***#
#***####################### DELETE  ############################***#
#***####################### ******* ############################***#
        
def delete_customer(lst):
    
    print ('...loading: update_customer()')
    
    print (lst)
    
    with conn:
        c.execute("""DELETE FROM dbcustomers WHERE name = :name""",
                 {
                'name': lst[1]
                })
        
        print ("Deleted customer %s" %lst[1])
        
        
#def delete_customer(lst):
#    
#    print ('...loading: update_customer()')
#    
#    print (lst)
#    
#    with conn:
#        c.execute("""DELETE FROM dbcustomers WHERE name = :name,
#                                                  address = :address,
#                                                  email = :email""",
#                 {
#                'name': lst[1], 
#                'address': lst[2],
#                'email': lst[3]
#                })
#        
#        print ("Deleted customer %s" %lst[1])


def remove_emp(emp):
    with conn:
        c.execute("DELETE from emplyoees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

def closedb():
    conn.close()
    
