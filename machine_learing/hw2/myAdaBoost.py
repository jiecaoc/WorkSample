# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:28:51 2013

@author: jiecaoc

A simple implementation of AdaBoost algorithm
"""
import numpy as np
from classes import DTree
import utilities as ut
import sys

def getWeakLearner(w, egs):
    """ 
    given: 
        a set of examples egs
        a distribution on the examples w
    return:
        a decision stump y that minimize
            J = \sum w_n I(y(x_n) \neq t_n)
    """
    record = 0
    error = 3171713.
    Nfeatures = len(egs[0]) - 1
    for i in range(Nfeatures):
        dt = DTree(lambda examples: i + 1)
        dt.training(egs, 1)
        tmp = weightedError(w, egs, dt)
        if tmp < error:
            error = tmp
            record = dt
    return record
    
def weightedError(w, egs, dt):
    N = len(egs)
    tmp = 0
    for i in range(N):
        tmp = tmp + w[i] * neq(dt.predict(egs[i]), egs[i][0])
    return tmp
       
 
def neq(a, b):
    return 1 if a != b else 0
    

def AdaBoost(examples, M):
    """
    given:
        examples
        M - the number of weak learner
    return:
        a function as the final model
    """
    # initialize the distribution w
    N = len(examples)
    w = [1.0 / N] * N
    y = [1] * M
    alpha = [1] * M
    # calculate 
    for m in range(M):
        y[m] = getWeakLearner(w, examples)
        # evaluate the error rate
        eps = weightedError(w, examples, y[m]) / sum(w)
        # get alpha
        alpha[m] = np.log((1 - eps) / eps)
        # update the distribution w
        for i in range(N):
            w[i] = w[i] * np.exp(alpha[m] * neq(y[m].predict(examples[i]), examples[i][0]))
    
    # construct the final model
    def Y(eg):
        tmp = 0
        for i in range(M):
            tmp = tmp + alpha[i] * y[i].predict(eg)
        return -1 if tmp < 0 else 1
    return lambda eg: Y(eg)
        
        

def cross_vad(examples, T, num_folds = 10):
    data = ut.dataCrossSplit(examples, num_folds, False)
    errorRates = []
    for i in range(num_folds):
        egs = data[i]
        classifier = AdaBoost(egs[0], T)
        # calculate error rate
        error = [0.] * 2
        for j in range(2):
            for x in egs[j]:
                if classifier(x) != x[0]:
                    error[j] = error[j] + 1
            error[j] = error[j] / len(egs[j])
        print "Fold ", i, " trainingData errorRate: ", error[0], " testData errorRate:", error[1]
        errorRates.append(error)
    arr = np.array(errorRates)
    print "Train Mean ErrorRate:", np.mean(arr[:,0]), " Test Mean ErrorRate:", np.mean(arr[:,1])
    print "Train StdVar ErrorRate:", np.sqrt(np.var(arr[:,0])), " Test Mean ErrorRate:", np.sqrt(np.var(arr[:, 1]))



if __name__ == '__main__':
    T = int(sys.argv[2])
    filename = sys.argv[1]
    egs = ut.importRawData(filename)
    egs = ut.preprocess(egs)
    print "T =", T
    cross_vad(egs, T)


