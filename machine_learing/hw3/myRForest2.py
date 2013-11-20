
import numpy as np
import classes as cls
import utilities as ut
import sys

def calcError(trainSet, testSet, numOfFeatures):
    """
        return [errorTrain, errorTest]
    """
    cl = cls.RandomForest(numOfFeatures)
    cl.training(trainSet)
    errors = [0] * 2
    # error on trainSet
    c = 0
    for eg in trainSet:
        if eg[0] != cl.predict(eg):
            c = c + 1
    errors[0] = (c + 0.) / len(trainSet)
    # error on testSet
    c = 0
    for eg in testSet:
        if eg[0] != cl.predict(eg):
            c = c + 1
    errors[1] = (c + 0.) / len(testSet)
    return errors

def cross_Valid(egs, numCross, M):
    crossData = ut.dataCrossSplit(egs, numCross, False)
    fold = 0
    errors = {}
    for x in M:
        errors[x] = [0] * numCross
    for i in range(numCross):
        data = crossData[i]
        print "# Fold", fold
        for b in M:
            print "  ", b, "Random Features:",
            err = calcError(data[0], data[1], b)
            print err
            errors[b][fold] = err
        fold = fold + 1
    return errors 

def getMean(errors, M):
    errs = {}
    for x in M:
        errs[x] = 0
    for b in M:
        errs[b] = np.mean(errors[b], 0).tolist()
    return errs

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Error, Check your input!"
        exit()
    filename = sys.argv[1]
    M = map(lambda x: int(x), sys.argv[2:])
    egs = ut.importRawData(filename)
    egs = ut.sampling(egs, len(egs))
    errors = cross_Valid(egs, 4, M)
    
    print getMean(errors, M)
    

