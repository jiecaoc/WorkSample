# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:43:58 2013

@author: jiecaoc
A simple implementation of multi-variate Gaussian generative 
multi-variate Gaussian generative 
"""

import utilities as ut
import numpy as np
from numpy.linalg import inv


def GaussianGM(trainData):
    """
        given a set of training data
        return a function f(x) as a classifier
        f(x) will return the class of x
    """
    K = len(trainData)
    # calculate p(C_k)
    p = [0] * (K)
    for i in range(K):
        p[i] = len(trainData[i + 1])
    N = sum(p)
    p = p / (N + .0)


    # calculate a_k (x)= W_k^T x + w_k0
    a = [1] * K
    sigma = [1] * K
    mu = [1] * K
    W = [1] * K
    w0 = [1] * K
    for i in range(K):
        mu[i] =  ut.getMean(trainData[i + 1], 'array')
        f = lambda x: np.dot((ut.ls2Vec(x) - mu[i]), (ut.ls2Vec(x) - mu[i]).transpose())
        sigma[i] = reduce(ut.add, map(f, trainData[i + 1]))
    sigma_inv = inv(reduce(ut.add, sigma) / (N + .0))

    for k in range(K):
        W[k] = np.dot(sigma_inv, mu[k])
        w0[k] = -0.5 * reduce(np.dot, [mu[k].transpose(), sigma_inv, mu[k]])[0,0] + np.log(p[k])
        a[k] = lambda x: np.dot(W[k].transpose(), ut.ls2Vec(x))[0,0] + w0[k]

    def f(w, w0, x):
        tmp = [ np.dot(ww.transpose(), ut.ls2Vec(x))[0,0] + ww0 
                for (ww, ww0) in zip(w, w0)
              ]  
        tmp = ut.getMaxPos(tmp)
        return tmp[0] + 1
    return lambda x: f(W, w0, x)


    




        
        
    
        