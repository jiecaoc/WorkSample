# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:34:31 2013

@author: Jiecao Chen (jieca001@umn.edu)
"""

import numpy as np  
import random


def importRawData(filePath):
    """
        import data in filePath
        return format data:
    """
    fin = open(filePath, 'r')
    data = map(lambda s: s.split(','), fin.read().splitlines())
    f = lambda ls: map(lambda s: float(s), ls)
    data = map(f, data)
    for i in range(len(data)):
        data[i][0] = int(data[i][0]) 
    fin.close()
    return data

def preprocess(rawData):
    """
        delete #11 features
    """
    for x in rawData:
        del x[11]
    return rawData

def hashData(rawData, num_classes = 3):
    """
        given rawData, return hashed data
    """
    result = {}
    for i in range(1, num_classes + 1):
        result[i] = [] 
    f = lambda ls: result[int(ls[0])].append(ls[1:])
    map(f, rawData)
    return result

def dataCrossSplit(rawData, num_cross, hashed = True):
    """
        return a dict of (trainDataSet, testDataSet),
        which have length num_cross
    """
    delta = len(rawData) / num_cross
    result = {}
    for i in range(num_cross):
        train = rawData[: i * delta] + rawData[(i + 1) * delta:]
        test = rawData[i * delta : min((i + 1) * delta, len(rawData))]
        if hashed:
            result[i] = (hashData(train), hashData(test))
        else:
            result[i] = (train, test)
    return result
        



def getSum(listOfFeatures, mode = 'list'):
    """
        calculate the sum of a list of features(vector)
    """
    f = lambda a, b: map(sum, zip(a, b))
    tmp = reduce(f, listOfFeatures)
    if mode == 'list':
        return tmp
    else:
        return np.array([tmp]).transpose()


def getMean(listOfFeatures, mode = 'list'):
    """
        calculate the mean of a list of features(vector)
    """
    length = len(listOfFeatures)
    tmp = map(lambda x: x / length, getSum(listOfFeatures))
    if mode == 'list':
        return tmp
    else:
        return np.array([tmp]).transpose()

def getMaxPos(ls, num = 1):
    """
        given a list,
        return the position of max elememt
    """
    tmp = sorted(zip(ls, range(len(ls))), key = lambda x: -x[0])
    tmp = map(lambda x: x[1], tmp)
    return tmp[: num]




def distance(v, u, d = 2):
    
    tmp = map(lambda x: pow(np.abs(x[0] - x[1]), d) / pow(np.abs(sum(x)), d), zip(v, u))
    return sum(tmp)
   
add = lambda x, y: x + y

def ls2Vec(ls):
    return np.array([ls]).transpose()
    
def makeDataRandom(aList):
    """
        given a list,
        return a list with random order
    """
    length = len(aList)
    for i in range(length * 10):
        a = random.randint(0, length - 1)
        b = random.randint(0, length - 1)
        if a != b:
            tmp = aList[a];
            aList[a] = aList[b]
            aList[b] = tmp
    return aList
    
def arrayExtract(arr, ls):
    
    return np.array([arr[:,i].tolist() for i in ls]).transpose()
        

def BootstrapSampling(examples):
    """
        given the examples,
        give a BootstrapSampling.
    """
    random.seed()
    K = len(examples)
    # print "K=", K
    egs = [1] * K
    for i in range(K):
        t = random.randint(0,K-1)
        egs[i] = examples[t]
    return egs

def sampling(S, N):
    """
        given a list S,
        random pick up N elements of it
    """
    random.seed()
    random.shuffle(S)
    return S[0:N]

 
   
    
    
# print makeDataRandom([1,2,3,4])
# test
#a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#print a
#print arrayExtract(a, [0,2])