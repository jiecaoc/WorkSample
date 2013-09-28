import random
import math
import sys
import numpy as np
# simple sample, return 1 with prob p
def sample(p):
    if random.random() <= p:
        return 1
    else:
        return 0

        
# Weighted-Sample
def Weight_Sample(e, numSteps):
    w = 1
    R = [1] * numSteps
    R[0] = sample(0.5)
    for i in range(numSteps - 1):
        if R[i] == 1:
            p = 0.7
        else:
            p = 0.3
        R[i + 1] = sample(p)
    # calculate weight
    for i in range(numSteps):
        if R[i] == 1:
            p = 0.9
        else:
            p = 0.2
        if e[i] == 0:
            p = 1 - p
        w = w * p

    return [w, R[numSteps - 1]]
        

# Likelihood-Weighing
def Likelihood_Weighting(e, numSteps, numSamples):
    W = [0, 0]
    for i in range(numSamples):
        [w, x] = Weight_Sample(e, numSteps)
        W[x] = W[x] + w

    length = sum(W)
    return [W[0] / length, W[1] / length]
        

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Input Error: argv not match!"
        exit()
    # numSamples = int(raw_input("numSamples: "))
    # numSteps = int(raw_input("numSteps: "))
    # evidence = list(raw_input("evidence sequence: "))
    numSamples = int(sys.argv[1])
    numSteps = int(sys.argv[2])
    evidence = list(sys.argv[3])
    e = [int(i) for i in evidence if i != ' ']
    if len(e) != numSteps:
        print "Input Error: length of sequence should matchs numSteps!"
        exit()

    results = []
    for rept in range(10):
        ans = Likelihood_Weighting(e, numSteps, numSamples)
        print "P(R_%d = T|u_1:%d) = %.4f" % (numSteps, numSteps, ans[1])
        print "P(R_%d = F|u_1:%d) = %.4f\n" % (numSteps, numSteps, ans[0])
        results.append(ans[1])
    print "After running 10 time, the varience of estimates is %.5f" % (np.var(results),)
