# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:03:35 2013

@author: jiecaoc
"""
import numpy as np
import utilities as ut
import operator as op

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
        self.threshold = []
    
    def predict(self, example):
        if self.next == {}:
            return self.label
        att = self.attribute
        flag = example[att] <= self.threshold[att]
        if (flag not in self.next.keys()):
            return self.label
        dt = self.next[flag]
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
        
        means = [1] * len(examples[0])
        for i in range(len(means)):
            means[i] = np.mean([eg[i] for eg in examples])#threshold(examples, i)#np.mean([eg[i] for eg in examples])
        self.threshold = means
        if height <= 0:
            return
        # select the attribute used in this node
        self.attribute = self.selectFunction(examples)
        # group the example based on the value on attribute
        for eg in examples:
            flag = (eg[self.attribute] <= means[self.attribute])
            if not flag in self.next.keys():
                self.next[flag] = DTree(self.selectFunction)
            self.next[flag].data.append(eg)
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
        
    def training(self, egs, depth = 2):
        for i in range(self.B):
            dt = DTree(SelectAtt)
            samples = ut.BootstrapSampling(egs)
            dt.training(samples, depth)
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


class RandomForest(classifierBagging):
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
            dt = DTree(lambda x: SelectAtt(x, featureSet))
            samples = ut.BootstrapSampling(egs)
            dt.training(samples, depth)
            self.trees[i] = dt 
        
    
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
    return -p1 * Log2(p1) - p2 * Log2(p2)

def Log2(x):
    if x <= 0.000001:
        return 100000
    else:
        return np.log2(x)

def ent(p1, p2):
    return  -p1 * Log2(p1) - p2 * Log2(p2)

def threshold(egs, att):
    """
        given egs and attribute,
        choose the `best` threshold for this att to construct binary decision tree
    """
    egs = sorted(egs, key = op.itemgetter(att))
    N = len(egs)
    c1 = [0] * len(egs)
    c = 0
    for eg in egs:
        if eg[0] == 1:
            if c == 0:
                c1[0] = 1
            else:
                c1[c] = c1[c-1] + 1
        c = c + 1
    info = [0] * len(egs)
    for i in range(len(egs) - 1):
        p1 = c1[i] / (i + 1)
        p2 = 1 - c1[i]
        q1 =  (c1[N-1] - c1[i]) / (N - i - 1)
        q2 = 1 - q1
        info[i] = -(i+1) / N * ent(p1, p2) - (N - i - 1) * ent(q1, q2)
    return egs[ut.getMaxPos(info)[0]][att]

def IG(examples, att):
    tmp = {}
    totlen = len(examples) + .0
    means = [1] * len(examples[0])
    for i in range(len(means)):
        means[i] = np.mean([eg[i] for eg in examples])#threshold(examples, i)#
        
    for eg in examples:
        flag = eg[att] <= means[att]
        if not (flag) in tmp.keys():
            tmp[flag] = []
        tmp[flag].append(eg)
    p = [(len(egs) / totlen * H(egs)) for egs in tmp.values()]
    ans = sum(p)
    return H(examples) - ans


    
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