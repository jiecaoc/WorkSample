# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:03:35 2013

@author: jiecaoc
"""
import numpy as np
import utilities as ut
#import operator as op
# N use to decide the number of intervals used to split the feature internal
N = 20


class DTree:
    """ 2 - layer decesion tree """
    def __init__(self, selectFun, features = range(33)):
        self.threshold = 0
        self.label = None
        self.left = None
        self.right = None
        self.att = 0
        self.selectAtt = selectFun 
        self.features = features
    
    def predict(self, eg, h = 2):
        if h == 0:
            return self.label
        if eg[self.att] <= self.threshold:
            dt = self.left
        else:
            dt = self.right
        if dt.label == None:
            return self.label
        return dt.predict(eg, h - 1)
    
    def training(self, egs, height = 2):
        if height <= 0:
            return
        self.label = findMost(egs)
        self.att = self.selectAtt(egs, self.features)
        # print self.label
        self.threshold = getThreshold(egs, self.att)
        self.left = DTree(self.selectAtt)
        self.left.training([eg for eg in egs if eg[self.att] <= self.threshold], height - 1)
        self.right = DTree(self.selectAtt)
        self.right.training([eg for eg in egs if eg[self.att] > self.threshold], height - 1)

#class DTree:
#    
#    def __init__(self, selectFun):
#        # this function will be use to split the data
#        # can be set as Information Gain, Gini Index etc
#        self.selectFunction = selectFun
#        self.attribute = ""
#        self.next = {}
#        self.data = []
#        self.label = ""
#        self.threshold = []
#    
#    def predict(self, example):
#        if self.next == {}:
#            return self.label
#        att = self.attribute
#        flag = example[att] <= self.threshold[att]
#        if (flag not in self.next.keys()):
#            return self.label
#        dt = self.next[flag]
#        return dt.predict(example)
#    
#    def printTree(self, block = ""):
#        if self.attribute == "":
#            return
#        print block, "#", self.attribute, "Attribute"
#        for v in self.next.keys():
#            print block, "|"
#            print block, "--", v,
#            if self.next[v].attribute == "":
#                print "-> Label:", self.next[v].label
#            else:
#                print "->"
#                self.next[v].printTree(block + "      ")
#            

    
#    def training(self, examples, height = 1):
#        self.label = findMost(examples)
#        
#        means = [1] * len(examples[0])
#        for i in range(len(means)):
#            means[i] = np.mean([eg[i] for eg in examples])#threshold(examples, i)#
#        self.threshold = means
#        if height <= 0:
#            return
#        # select the attribute used in this node
#        self.attribute = self.selectFunction(examples)
#        # group the example based on the value on attribute
#        for eg in examples:
#            flag = (eg[self.attribute] <= means[self.attribute])
#            if not flag in self.next.keys():
#                self.next[flag] = DTree(self.selectFunction)
#            self.next[flag].data.append(eg)
#        # now we need to train the next level
#        for key in self.next.keys():
#            dt = self.next[key]
#            dt.training(dt.data, height - 1)
#            # after training, release the data space
#            dt.data = []
 

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
            dt.training(samples)
            self.trees[i] = dt
    
    def predict(self, eg):
        """
            given an example
            make a prediction
        """
        return findMost([[dt.predict(eg)] for dt in self.trees])




class RandomForest:
    """
        A simply implementation of 
        Random Forest
    """            
    def __init__(self, numOfFeatures, numOfBases = 100):
        self.m = numOfFeatures
        self.B = numOfBases
        self.trees = [1] * self.B
    
    def training(self, egs, depth = 2):
        for i in range(self.B):
            featureSet = ut.sampling(range(len(egs[0]) - 1), self.m)
            # print featureSet
            dt = DTree(SelectAtt, featureSet)
            samples = ut.BootstrapSampling(egs)
            dt.training(samples, depth)
            self.trees[i] = dt 

    def predict(self, eg):
        """
            given an example
            make a prediction
        """
        return findMost([[dt.predict(eg)] for dt in self.trees])       
    
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
    if examples == []:
        return 0
    totlen = len(examples) + .0
    count = {}
    count[1] = count[2] = 0
    for eg in examples:
        count[eg[0]] = count[eg[0]] + 1
    p1 = count[1] / totlen
    p2 = count[2] / totlen
    return -p1 * Log2(p1) - p2 * Log2(p2)

def Log2(x):
    if x <= 0.000001:
        return 100000
    else:
        return np.log2(x)

def ent(p1, p2):
    return  -p1 * Log2(p1) - p2 * Log2(p2)


def getThreshold(egs, att):
    """
        given egs and attribute,
        choose the `best` threshold for this att to construct binary decision tree
    """
    if egs == []:
        return 0
    tmp = [eg[att] for eg in egs]
    mn = min(tmp)
    delta = (max(tmp) - min(tmp)) / N
    tmp = [ig(egs, att, i * delta + mn) for i in range(N)]
    return ut.getMaxPos(tmp)[0] * delta + mn
        


def ig(examples, att, threshold):
    if examples == []:
        return 0
    totlen = len(examples) + .0
    # threshold = getThreshold(examples, att)
    #threshold(examples, i)#
    left = [eg for eg in examples if eg[att] <= threshold]
    right = [eg for eg in examples if eg[att] > threshold]
    return H(examples) - len(left) / totlen * H(left) - len(right) / totlen * H(right)

def IG(egs, att):
    return ig(egs, att, getThreshold(egs, att))


    
def SelectAtt(examples, featureSet = []):
    """ select the best attribute 
        to split the examples,
        Based on IG
    """
    if len(featureSet) == 0:
        featureSet = range(len(examples[0]) - 1)
    p = [IG(examples, i + 1) for i in featureSet]
    ans = ut.getMaxPos(p)
    #print p[ans[0]]
    return ans[0] + 1