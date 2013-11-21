
import numpy as np
import classes as cls
import utilities as ut
import sys
import random

def calcError(trainSet, testSet, numOfBase):
    """
        return [errorTrain, errorTest]
    """
    cl = cls.classifierBagging(numOfBase)
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

def cross_Valid(egs, numCross, B):
    crossData = ut.dataCrossSplit(egs, numCross, False)
    fold = 0
    errors = {}
    for x in B:
        errors[x] = [0] * numCross
    for i in range(numCross):
        data = crossData[i]
        print "# Fold", fold
        for b in B:
            print "  ", b, "Bases:",
            err = calcError(data[0], data[1], b)
            print err
            errors[b][fold] = err
        fold = fold + 1
    return errors 

def getMeanStd(errors, B):
    errs = {}
    variances = {}
    for x in B:
        errs[x] = 0
        variances[x] = 0
    for b in B:
        errs[b] = np.mean(errors[b], 0).tolist()
        variances[b] = np.std(errors[b], 0).tolist()
    print "# average errors in form of [trainData, testData]:"
    for b in B:
        print "  ", b, "bases:", errs[b]
    print "# std derivation in form of [trainData, testData]:"
    for b in B:
        print "  ", b, "bases:", variances[b]
    return (errs, variances)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Error, Check your input!"
        exit()
    filename = sys.argv[1]
    B = map(lambda x: int(x), sys.argv[2:])
    egs = ut.importRawData(filename)
    random.seed()
    random.shuffle(egs)
    errors = cross_Valid(egs, 10, B)
    
    tmp = getMeanStd(errors, B)
    means = tmp[0]
    stds = tmp[1]
    print [means[i][0] for i in B]
    print [means[i][1] for i in B]
    print " ===== "
    print [stds[i][0] for i in B]
    print [stds[i][1] for i in B]
    
    

