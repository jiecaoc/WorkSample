# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:03:35 2013

@author: jiecaoc
"""

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
        
    
def findMost(examples):
    tmp = {}
    tmp[-1] = tmp[1] = 0
    for eg in examples:
        tmp[eg[0]] = tmp[eg[0]] + 1
    if tmp[-1] > tmp[1]:
        return -1
    else:
        return 1