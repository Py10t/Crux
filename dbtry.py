# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:04:54 2018

@author: andra
"""

import sqlite3
from basedata import Employee

#conn = sqlite3.connect('employee.db') 
#wäre der Befehl um harddrive statt ram zu nutzen
conn = sqlite3.connect(':memory:')
#nutzt :memory: d.h. ram

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")



c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))



def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

        
def remove_emp(emp):
    with conn:
        c.execute("DELETE from emplyoees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})
        
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

enps = get_emps_by_name('Doe')
conn.close()