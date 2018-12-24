# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:30:38 2018

@author: icytanz
"""

import copy

def get_mul_factor(num,result=[]):
    if(num==1):
        total=copy.copy(result)
        if 1 not in total:
            total.append(1)
        print(total)
        return
    elif(num<1):
        return
    else:
        n=list(range(num+1))
        n.reverse()
        if 1 in result:
            m=range(len(n)-2)
        else:
            m=range(len(n)-1)
        for i in m:
            new_result=copy.copy(result)
            if num%n[i]==0:
                new_result.append(n[i])
                get_mul_factor(num//n[i],new_result)
                
if __name__=='__main__':
    get_mul_factor(2)
    
    get_mul_factor(1)
    
    get_mul_factor(4)
    
    get_mul_factor(6)
    
    get_mul_factor(8)
