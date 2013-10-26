# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:37:49 2013

@author: jiecaoc
"""
import numpy as np
from classes import DTree
import utilities as ut


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
    # final model
    g = 0
    # calculate 
    for m in range(M):
        y[m] = getWeakLearner(w, examples)
        # evaluate the error rate
        eps = weightedError(w, examples, y[m]) / sum(w)
        # get alpha
        alpha[m] = np.log((1 - eps) / eps)
        # update the final model
        g = lambda eg: sum([alpha[i] * y[i].predict(eg) for i in range(m)])  
        # update the distribution w
        for i in range(N):
            sign = 1 if g(examples[i]) > 0 else -1
            w[i] = 1 / (1 + np.exp(examples[i][0] * sign))
        tmp = sum(w)
        w = [v / tmp for v in w]
    
    # construct the final model
    def Y(eg):
        tmp = 0
        for i in range(M):
            tmp = tmp + alpha[i] * y[i].predict(eg)
        return -1 if tmp < 0 else 1
    return lambda eg: Y(eg)
        
egs = ut.importRawData('Mushroom.csv')
N = len(egs)
w = [1. / N] * N

dt = AdaBoost(egs, 5)
for i in range(500):
    if egs[i][0] != dt(egs[i]):
        print dt(egs[i]), '\n', egs[i]