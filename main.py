'''
Created on 2013-3-14

@author: Administrator
'''

from Verilog.CMultiply import CMultiply
#from Verilog.BMBooth import *

if __name__ == '__main__':
    
    
    for i in range(5,65):
        for j in range(5,i+1):
            c= CMultiply()
            c.makeMultiply(i,j)   
    
    
    
        #print i
    
    
    """
    c= CMultiply()
    c.makeMultiply(15,15)   
    
    
    c= CMultiply()
    c.makeMultiply(14,12)  
    
    c= CMultiply()
    c.makeMultiply(16,13)  
    
    c= CMultiply()
    c.makeMultiply(19,15)    
    #c.displayCode()
    """
        
    