
import numpy as np
import classes as cls
import utilities as ut

B = 5


egs = ut.importRawData('Ionosphere.csv')
classifier = cls.classifierBagging(B)
classifier.training(egs)

for i in range(300):
    eg = egs[i]
    print eg[0], classifier.predict(eg)
    


