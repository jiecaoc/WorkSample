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
    data = map(lambda s: s.split(';'), fin.read().splitlines())
    f = lambda ls: map(lambda s: int(s), ls)
    data = map(f, data)
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
    K = len(examples)
    egs = [1] * K
    for i in range(K):
        egs[i] = examples[random.randint(0,K)]
    return egs
    

 def H(examples):
    """
        calculate the entropy of examples
    """
    totlen = len(examples) + .0
    count = {}
    count[1] = count[2] = 0
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
   
    
    
# print makeDataRandom([1,2,3,4])
# test
#a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#print a
#print arrayExtract(a, [0,2])