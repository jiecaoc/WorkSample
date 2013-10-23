# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:47:34 2013

@author: jiecaoc
"""
import utilities as ut
from classes import DTree 

def Gini(examples):
    """
        calculate the Gini Index of examples
    """
    totlen = len(examples) + .0
    count = {}
    count[-1] = count[1] = 0
    for eg in examples:
        count[eg[0]] = count[eg[0]] + 1
    p1 = count[-1] / totlen
    p2 = count[1] / totlen
    return p1 * p2

def GI(examples, att):
    tmp = {}
    totlen = len(examples) + .0
    for eg in examples:
        if not eg[att] in tmp.keys():
            tmp[eg[att]] = []
        tmp[eg[att]].append(eg)
    p = [(len(egs) / totlen * Gini(egs)) for egs in tmp.values()]
    ans = sum(p)
    return Gini(examples) - ans
    
def SelectAtt(examples):
    """ select the best attribute 
        to split the examples,
        Based on IG
    """
    length = len(examples[0])
    p = [GI(examples, i + 1) for i in range(length - 1)]
    ans = ut.getMaxPos(p)
    # print p[ans[0]]
    return ans[0] + 1

# now test ,
# print out the wrong predictions
dt =  DTree(SelectAtt) 
egs = ut.importRawData('Mushroom.csv')
print SelectAtt(egs)
dt.training(egs, 2)
for i in range(8000):
    if egs[i][0] != dt.predict(egs[i]):
        print dt.predict(egs[i]), '\n', egs[i]