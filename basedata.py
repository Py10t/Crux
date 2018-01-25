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
        self.intID = 0
        self.extID = 0
        #amount right now produced on the machine
        self.manufacturing = 0
        #tbm = to be manufactured like still waiting or left for a deadline
        self.tbm = 0
        #ppc = price per 100
        self.ppcent = 0
        #mincost = calculated minimum
        self.mincost = 0
        self.weight = 0
        #dimensions should lead to a drawing or something like that
        self.dimensions = 0
        #material should be linked to a material in db
        self.material = 0
        self.stock = 0
        
#material
        self.company = 0
        self.price = 0