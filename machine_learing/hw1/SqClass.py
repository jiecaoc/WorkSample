# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 00:41:10 2013

@author: Jiecao Chen (jieca001@umn.edu)

Least Squares for Classification
"""
import numpy as np
import utilities as ut
import sys

def cross_validation(crossData, K = 3):
    """
        given a cross training set
        return the error rate
    """
    num_cross = len(crossData)
    totError = 0
    totNum = 0
    for i in range(num_cross):
        f = leastSquare(crossData[i][0])
        for x in crossData[i][1]:
            totNum = totNum + 1
            if ut.getMaxPos(f(x[1:]).tolist())[0] != x[0] - 1:
                totError = totError + 1
    return (totError + 0.) / totNum

def classEncode(classLabel):
    tmp = [0] * 3
    tmp[int(classLabel) - 1] = 1
    return tmp

def leastSquare(trainData, K = 3):
    """
        give training data,
        return f(x), defined as f(x) = W'x
    """
    # construct Y
    Y = np.array([classEncode(x[0]) for x in trainData])
    # construct X
    X = np.array([ x[1:] for x in trainData])
    X_ = np.dot( np.linalg.inv( np.dot(X.transpose(), X) ), X.transpose() )
    W_T = np.dot(X_, Y).transpose()
    return lambda x: np.dot(W_T, x)
    

# check input
if len(sys.argv) != 3:  
    print "input error"
    exit()
fileName = sys.argv[1]
num_cross = int(sys.argv[2])

rawData = ut.makeDataRandom(ut.importRawData(fileName))


crossData = ut.dataCrossSplit(rawData, num_cross, False)
print "Data: ", fileName
print "Error rate for cross_validation:", cross_validation(crossData)



