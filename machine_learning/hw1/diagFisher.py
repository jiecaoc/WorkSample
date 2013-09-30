# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:34:31 2013

@author: Jiecao Chen (jieca001@umn.edu)
"""

import LDAClasses as lda
import utilities as ut



# import data
rawData = ut.importRawData('Iris.csv')
trainData = ut.dataCrossSplit(rawData, 10)

cl = lda.Classifier()
cl.training(trainData[0][0])

for x in trainData[8][1][3]:
    print cl.classify(x)
