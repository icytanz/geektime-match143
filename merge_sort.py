# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:56:42 2018

@author: icytanz
"""

def merge(a,b):
    if a==None:
        a=[]
    if b==None:
        b=[]
        
    c=[]
    ai=0
    bi=0
    while ai<len(a) and bi<len(b):
        if a[ai]<b[bi]:
            c.append(a[ai])
            ai+=1
        else:
            c.append(b[bi])
            bi+=1
            
    if ai<len(a):
        c.extend(a[ai:])
    if bi<len(b):
        c.extend(b[bi:])
    
    return c
    
def merge_sort(to_sort):
    if to_sort==None:
        return []
    if len(to_sort)==1:
        return to_sort
    
    mid=len(to_sort)//2
    left=to_sort[0:mid]
    right=to_sort[mid:]
    
    left=merge_sort(left)
    right=merge_sort(right)
    
    merged=merge(left,right)
    return merged

if __name__=='__main__':
    
    a=[1,3,5,7]
    b=[2,4,7,11]
    
    merge(a,b)
    
    to_sort=[1,5,3,9,2,18,7]
    print(merge_sort(to_sort))
