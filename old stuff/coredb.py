# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:01:12 2018

@author: andrasz
"""

import sqlite3

conn = sqlite3.connect('coredatabase.db')

c = conn.cursor()

# c.execute("""DROP TABLE dir_values""")

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

# c.execute(""" CREATE TABLE dir_values (
#            file_name text,
#            path_var text,
#            intID int,
#            time date
#            )""")
#
# c.execute(""" CREATE TABLE utility_values (
#            db_name text,
#            last_intID int
#            )""")

#c.execute(""" CREATE TABLE dbcustomers (
#            intID int,
#            name text,
#            address text,
#            email text,
#            time date
#            )""")
#
#c.execute(""" CREATE TABLE dbarticles (
#            intID int,
#            name text,
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
#            intID int,
#            name text,
#            material text,
#            company text,
#            price real,
#            time date
#            )""")
#
#c.execute(""" CREATE TABLE dbmachines (
#            intID int,
#            name text,
#            machine_group int,
#            time date
#            )""")
#
#c.execute(""" CREATE TABLE work_orders (
#            intID int,
#            article_name text,
#            machine_group int,
#            delivery_date = text,
#            status = text,
#            time date
#            )""")
#
#c.execute(""" CREATE TABLE tools (
#            intID int,
#            name text,
#            machine_group int,
#            time date
#            )""")
#
    

#***####################### ******* ############################***#
#***####################### INSERT #############################***#
#***####################### ******* ############################***#

def insert_newcustomer(lst):
    
    print ('...loading: insert_newcustomer()')
    
    with conn:
       c.execute("""INSERT INTO dbcustomers VALUES (:intID, :name, :address, :email, :time)""",
                 {
                'intID' : lst[1],
                'name': lst[2],
                'address': lst[3],
                'email': lst[4],
                'time' : lst[5]
                })

def insert_newarticle(lst):
    
    print ('...loading: insert_newarticle()')
    
    with conn:
       c.execute("""INSERT INTO dbarticles VALUES (:intID, :name, :extID, :weight, :ppcent, :cavities, :cycle_time, :material, :time)""",
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
    
    print ("Finished inserting new article -> %s" %lst[2])
    
def insert_newmaterial(lst):
    
    print ('...loading: insert_newstuff()')
    
    with conn:
       c.execute("""INSERT INTO dbmaterials VALUES (:intID, :name, :material, :company, :price, :time)""",
                 {
                'name': lst[2],
                'intID': lst[1],
                'material': lst[3],
                'company': lst[4],
                'price': lst[5],
                'time' : lst[6]
                })


def insert_new_path(lst):

    print('...loading: insert_new_path()')
    print(lst)

    with conn:
        c.execute("""INSERT INTO dir_values VALUES (:file_name, :path_var, :intID, :time)""",
                  {
                      'file_name': lst[0],
                      'path_var': lst[1],
                      'intID': lst[2],
                      'time': lst[3]
                  })

    print("Finished inserting new path -> %s" % lst[1])
#    customer = [1,2,3]
#    articles = [1,4,5,6,7,10]
#    material = [1,10,11,12]

#***####################### ******* ############################***#
#***####################### READ Table #########################***#
#***####################### ******* ############################***#

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

# def get_all_articles():
#
#     print ('...loading: get_all_articles()')
#
#     c.execute("SELECT * FROM dbarticles")
#     return (c.fetchall())

def get_path_var(x):

    print ('...loading: get_all_articles()')

    c.execute("SELECT path_var FROM dir_values WHERE intID = :intID", {'intID' : x})
    return (c.fetchall())

def get_all_articles():

    print ('...loading: get_all_articles()')

    c.execute("SELECT intID, name, ppcent, material FROM dbarticles")
    return (c.fetchall())

def get_all_materials():
    
    print ('...loading: get_all_materials(), hier simma')

    c.execute("SELECT * FROM dbmaterials")
    return (c.fetchall())

def get_intID(x):

    print('...loading: get_all_intIDs()')

    c.execute("SELECT last_intID FROM utility_values WHERE db_name = :db_name", {'db_name = x'})
    return (c.fetchone())


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


def delete_dir_values(lst):

    print('...loading: delete_dir_values()')

    print(lst)

    with conn:
        c.execute("""DELETE FROM dir_values WHERE file_name = :name""",
                  {
                      'name': lst
                  })

        print("Deleted dir_value with file_name %s" % lst)


def remove_emp(emp):
    with conn:
        c.execute("DELETE from emplyoees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

def closedb():
    conn.close()
    
