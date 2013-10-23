# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:53:09 2013

@author: jiecaoc
"""
import numpy as np
import utilities as ut
from classes import DTree 

def H(examples):
    """
        calculate the entropy of examples
    """
    totlen = len(examples) + .0
    count = {}
    count[-1] = count[1] = 0
    for eg in examples:
        count[eg[0]] = count[eg[0]] + 1
    p1 = count[-1] / totlen
    p2 = count[1] / totlen
    def Log2(x):
        if x <= 0.000001:
            return 100000
        else:
            return np.log2(x)
    return -p1 * Log2(p1) - p2 * Log2(p2)


def IG(examples, att):
    tmp = {}
    totlen = len(examples) + .0
    for eg in examples:
        if not eg[att] in tmp.keys():
            tmp[eg[att]] = []
        tmp[eg[att]].append(eg)
    p = [(len(egs) / totlen * H(egs)) for egs in tmp.values()]
    ans = sum(p)
    return H(examples) - ans
    
def SelectAtt(examples):
    """ select the best attribute 
        to split the examples,
        Based on IG
    """
    length = len(examples[0])
    p = [IG(examples, i + 1) for i in range(length - 1)]
    ans = ut.getMaxPos(p)
    print p[ans[0]]
    return ans[0] + 1

dt =  DTree(SelectAtt) 
egs = ut.importRawData('Mushroom.csv')
print SelectAtt(egs)
dt.training(egs, 1)
for i in range(5000):
    if egs[i][0] != dt.predict(egs[i]):
        print dt.predict(egs[i]), '\n', egs[i]