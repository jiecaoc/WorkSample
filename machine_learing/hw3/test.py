# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:55:53 2013

@author: jiecaoc
"""

import utilities as ut
import classes as cls

egs = ut.importRawData('Ionosphere.csv')


raw = ut.dataCrossSplit(egs, 2, False)
dt = cls.DTree(cls.SelectAtt)
dt.training(raw[0][0])
c = 0
for eg in raw[0][1]:
    if eg[0] != dt.predict(eg):
        # print eg[0], dt.predict(eg)
        c = c + 1
print (c + .0) / len(egs)