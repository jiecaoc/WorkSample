# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:34:31 2013

@author: Jiecao Chen (jieca001@umn.edu)
"""

import numpy as np

def importRawData(filePath):
    """
        import data in filePath
        return format data:
    """
    fin = open(filePath, 'r')
    data = map(lambda s: s.split(','), fin.read().splitlines())
    f = lambda ls: map(lambda s: float(s), ls)
    data = map(f, data)
    fin.close()
    return data

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

def dataCrossSplit(rawData, num_cross):
    """
        return a dict of (trainDataSet, testDataSet),
        which have length num_cross
    """
    delta = len(rawData) / num_cross
    result = {}
    for i in range(num_cross):
        train = rawData[: i * delta] + rawData[(i + 1) * delta:]
        test = rawData[i * delta : min((i + 1) * delta, len(rawData))]
        result[i] = (hashData(train), hashData(test))
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

def getMaxPos(ls):
    """
        given a list,
        return the position of max elememt
    """
    return max( zip(ls, range(len(ls))) )[1]
    

   
add = lambda x, y: x + y

def ls2Vec(ls):
    return np.array([ls]).transpose()
# test
#print getMaxPos([3,1,2,5,6,1])