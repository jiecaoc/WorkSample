# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:53:09 2013

@author: jiecaoc
"""
import numpy as np
import utilities as ut
from classes import DTree 
import sys

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
    #print p[ans[0]]
    return ans[0] + 1


def cross_vad(examples, num_folds = 10):
    data = ut.dataCrossSplit(examples, num_folds, False)
    errorRates = []
    for i in range(num_folds):
        egs = data[i]
        dt = DTree(SelectAtt)
        dt.training(egs[0], 1)
        # calculate error rate
        error = [0.] * 2
        for j in range(2):
            for x in egs[j]:
                if dt.predict(x) != x[0]:
                    error[j] = error[j] + 1
            error[j] = error[j] / len(egs[j])
        print "Fold ", i, " trainingData errorRate: ", error[0], " testData errorRate:", error[1]
        errorRates.append(error)
    arr = np.array(errorRates)
    print "Train Mean ErrorRate:", np.mean(arr[:,0]), " Test Mean ErrorRate:", np.mean(arr[:,1])
    print "Train StdVar ErrorRate:", np.sqrt(np.var(arr[:,0])), " Test Mean ErrorRate:", np.sqrt(np.var(arr[:, 1]))

if __name__ == '__main__':
    filename = sys.argv[1]
    egs = ut.importRawData(filename)
    cross_vad(egs)
    dt = DTree(SelectAtt)
    dt.training(egs)
    print "========= the decision tree ============"
    dt.printTree()
