# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:03:35 2013

@author: jiecaoc
"""
import numpy as np
import utilities as ut

class DTree:
    """ Decision Tree Model """
    def __init__(self, selectFun):
        # this function will be use to split the data
        # can be set as Information Gain, Gini Index etc
        self.selectFunction = selectFun
        self.attribute = ""
        self.next = {}
        self.data = []
        self.label = ""
    
    def predict(self, example):
        if self.next == {}:
            return self.label
        att = self.attribute
        dt = self.next[example[att]]
        return dt.predict(example)
    
    def printTree(self, block = ""):
        if self.attribute == "":
            return
        print block, "#", self.attribute, "Attribute"
        for v in self.next.keys():
            print block, "|"
            print block, "--", v,
            if self.next[v].attribute == "":
                print "-> Label:", self.next[v].label
            else:
                print "->"
                self.next[v].printTree(block + "      ")
            

    
    def training(self, examples, height = 1):
        self.label = findMost(examples)
        if height <= 0:
            return
        # select the attribute used in this node
        self.attribute = self.selectFunction(examples)
        # group the example based on the value on attribute
        for eg in examples:
            if not eg[self.attribute] in self.next.keys():
                self.next[eg[self.attribute]] = DTree(self.selectFunction)
            self.next[eg[self.attribute]].data.append(eg)
        # now we need to train the next level
        for key in self.next.keys():
            dt = self.next[key]
            dt.training(dt.data, height - 1)
            # after training, release the data space
            dt.data = []
 

class classifierBagging:
    """
        Classifier using bagging approach
    """
    def __init__(self, numberOfBases):
        self.B = numberOfBases
        self.trees = [1] * self.B
        
    def training(self, egs):
        for i in range(self.B):
            dt = DTree(SelectAtt)
            samples = ut.BootstrapSampling(egs)
            dt.training(samples, 2)
            self.trees[i] = dt
    
    def predict(self, eg):
        """
            given an example
            make a prediction
        """
        result = [1] * self.B
        for i in range(self.B):
            result[i] = [self.trees[i].predict(eg)]
        return findMost(result)
            
    
def findMost(examples):
    tmp = {}
    tmp[1] = tmp[2] = 0
    for eg in examples:
        tmp[eg[0]] = tmp[eg[0]] + 1
    if tmp[1] > tmp[2]:
        return 1
    else:
        return 2


def H(examples):
    """
        calculate the entropy of examples
    """
    totlen = len(examples) + .0
    count = {}
    count[1] = count[2] = 0
    for eg in examples:
        count[eg[0]] = count[eg[0]] + 1
    p1 = count[1] / totlen
    p2 = count[2] / totlen
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
    #print p[ans[0]]
    return ans[0] + 1