# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:34:31 2013

@author: Jiecao Chen (jieca001@umn.edu)
"""

import LDAClasses as lda
import utilities as ut
import sys


def cross_validation(crossData, subSpaceDim):
    """
        given a cross training set
        return the error rate
    """
    num_cross = len(crossData)
    totError = 0
    totNum = 0
    for i in range(num_cross):
        cl = lda.Classifier()
        # set S_W as diag matrix I
        cl.training(crossData[i][0], 'diag', subSpaceDim)
        for k in range(1, len(crossData[i][1]) + 1):
            for x in crossData[i][1][k]:
                totNum = totNum + 1
                if cl.classify(x) != k:
                    totError = totError + 1
    return (totError + 0.) / totNum
            

# check input
if len(sys.argv) != 3:  
    print "input error"
    exit()
fileName = sys.argv[1]


    
num_cross = int(sys.argv[2])
# import data
# since the date in the file are in order
# need to make it random to run cross validation
rawData = ut.makeDataRandom(ut.importRawData(fileName))
rawData = ut.importRawData(fileName)
trainData = ut.dataCrossSplit(rawData, num_cross)

if fileName == 'Iris':
    subSpaceDim = 3
else:
    subSpaceDim = 9


#print tmp[1]
print "Data: ", fileName
print "Error rate for cross_validation:", cross_validation(trainData, subSpaceDim)
