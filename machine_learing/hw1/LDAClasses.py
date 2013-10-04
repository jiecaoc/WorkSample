# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:03:02 2013

@author: Jiecao Chen (jieca001@umn.edu)

An simply implimentation for multi-classes Fisher's Liear Discriminant Classifier 
Based on analysis of Bishop's Pattern Recognization and Machine Learning
"""
import numpy as np
import utilities as ut
import GaussianGM

class Classifier:
    """
        imput:  list of (label, value) pair
    """
    def __init__(self):
#        self.labelValuePairs = ls
#        self.func = func
        "new class created"

    
        
    
    def classify(self, value):
        return self.func(self.projectFunc(value))
  
  
    def training(self, trainData, mode = 'diag', subSpaceDim = 2):
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
        S_W = []
        Sk = range(K + 1)
        if mode == 'diag':
            S_W = np.diag([1] * D)
        else:
            g = lambda x, y: np.dot((x - y), (x - y).transpose())
            for k in range(1, K + 1 ):
                Sk[k] = reduce(ut.add, [g(ut.ls2Vec(x), mk[k]) for x in trainData[k]])
                      
            S_W = reduce(ut.add, Sk[1:])
        #
        [egs, vecs] = np.linalg.eigh(np.dot(np.linalg.inv(S_W), S_B))
        
         
        pos = ut.getMaxPos(egs, subSpaceDim)
        
        W = ut.arrayExtract(vecs, pos)

        # now we will construct trainingData set in the
        # sub-feature space, then run Gaussian generative 
        # method to train the new trainData set to get a
        # a classifier
        def projectFunc(v):
            tmp = np.dot(ut.ls2Vec(v).transpose(), W).tolist()
            return tmp[0]
        for k in range(K):
            trainData[k + 1] = map(projectFunc, trainData[k + 1])
        self.projectFunc = projectFunc
        self.func = GaussianGM.GaussianGM(trainData)

        


