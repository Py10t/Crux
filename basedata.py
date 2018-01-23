# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:52:49 2017

@author: Andrasz
"""
    
    
class Stammdaten:


    def __init__(self):
        #invoking all attr. on object
        
        self.name = 0
        
        #customer
        self.address = 0
        self.email = 0 
        
        #article
        self.interneBez = 0
        self.externeBez = 0
        self.weight = 0
        self.manufacturing = 0
        self.zufertigen = 0
        self.ppcent = 0
        self.mincost = 0
        self.dimensions = 0
        self.material = 0
        self.stock = 0
        
        #material
        self.company = 0
        self.price = 0
        
        
class Employee:
    
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay