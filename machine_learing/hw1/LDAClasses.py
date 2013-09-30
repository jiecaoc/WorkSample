# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:03:02 2013

@author: Jiecao Chen (jieca001@umn.edu)

An simply implimentation for multi-classes Fisher's Liear Discriminant Classifier 
Based on analysis of Bishop's Pattern Recognization and Machine Learning
"""
import numpy as np
import utilities as ut

class Classifier:
    """
        imput:  list of (label, value) pair
    """
    def __init__(self):
#        self.labelValuePairs = ls
#        self.func = func
        "new class created"
    
    def classify(self, value):
        # find the most possible label for value
        best = (0, 10000000)
        for p in self.labelValuePairs:
            if np.linalg.norm(self.func(value) - p[1]) < best[1]:
                best = (p[0], np.linalg.norm(self.func(value) - p[1]))
        return best[0]
  
  
    def training(self, trainData, mode = 'diag'):
        # num of classes
        K = len(trainData)
        # num of features
        D = len(trainData[1][0])
        #
        mk = {}
        for k in range(1, K + 1):
            mk[k] = ut.getMean(trainData[k], 'array')
        #
        m = ut.getMean(reduce(ut.add, [trainData[k] for k in range(1, K + 1)]))
        
        #
        f = lambda k: len(trainData[k]) * np.dot( mk[k] - m, (mk[k] - m).transpose() )
        S_B = reduce(ut.add, [f(k) for k in range(1, K - 1)])
        # construct S_W
        if mode == 'diag':
            S_W = np.diag([1] * D)
        #
        [egs, vecs] = np.linalg.eigh(S_B)
        # we alway chose the max eigenvlue
        # which means D features will be projected into 1 feature
        pos = ut.getMaxPos(egs)
        W = np.dot(np.linalg.inv(S_W), np.array(vecs[:, pos:(pos+1)]))

        # construct the test function
        func = lambda v: np.dot(W.transpose(), ut.ls2Vec(v))
        self.func = func
        labelValues = []

        for k in range(1, K + 1):
            tmp = [ (x[0:].transpose())[0].tolist() for x in map(func, trainData[k]) ]
            mean = ut.getMean(tmp)
            labelValues.append((k, mean))
        self.labelValuePairs = labelValues
