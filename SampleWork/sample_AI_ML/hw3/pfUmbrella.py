import random
import sys
import numpy as np

def get_initial(N):
    """
    inputs:
    N:

    outputs: a vector of samples generated from P(X_0)
    """
    S = [1] * N
    for i in range(N):
        if random.random() <= 0.5:
            S[i] = 1
        else:
            S[i] = 0
    return S

    
def Weighted_Sample(N, S, W):
    """
    Random weighted sample
    """
    new_S = [1] * N
    total = sum(W)
    for n in range(N):
        i = 0
        remain = random.random() * total
        while (i < N) & (remain > W[i]):
            remain = remain - W[i]
            i = i + 1
        if i == N:
            i = i - 1
        new_S[n] = S[i]
    return new_S
            
    
def Particle_Filtering(e, N, S):
    """
    inputs:
    e: environment
    N: the number of samples to maintain
    Samples: vectors of current samples
    outputs: a set of samples for the next time step
    """
    # S = get_initial(N)
    W = [0] * N

    for i in range(N):
        if S[i] == 1:
            p = 0.7
        else:
            p = 0.3
        if random.random() <= p:
            S[i] = 1
        else:
            S[i] = 0
            
        if S[i] == 1:
            p = 0.9
        else:
            p = 0.2
        if (e == 0):
            p = 1 - p
        W[i] = p
    S = Weighted_Sample(N, S, W)
    return S

    
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
    ans = []
    for rept in range(10):    
        S = get_initial(numSamples)
        for n in range(numSteps):
            S = Particle_Filtering(e[n], numSamples, S)
        S = [i for i in S if i == 1]
        p = (len(S) + .0) / numSamples
        print "P(R_%d = T|u_1:%d) = %.4f" % (numSteps, numSteps, p)
        print "P(R_%d = F|u_1:%d) = %.4f\n" % (numSteps, numSteps, 1 - p)
        ans.append(p)
    
    print "After running 10 time, the varience of estimates is %.5f"% (np.var(ans),)
    
