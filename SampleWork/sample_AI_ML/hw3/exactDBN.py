# Exact calculation of Filtering
import sys
import numpy as np


def normalize(s):
    s = s.tolist()
    tot = sum(s)
    s = [(i + 0.0) / tot for i in s]
    return np.array(s)


def forward(f, e):
    tmp = np.array([0.7, 0.3]) * f[0] + np.array([0.3, 0.7]) * f[1] 
    ls = [0.9, 0.2]
    if e == 0:
        ls = [(1 - p) for p in ls]
    return normalize(tmp * np.array(ls))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Input Error: argv not match!"
        exit()
    # numSamples = int(raw_input("numSamples: "))
    # numSteps = int(raw_input("numSteps: "))
    # evidence = list(raw_input("evidence sequence: "))
#    numSamples = int(sys.argv[1])
    numSteps = int(sys.argv[1])
    evidence = list(sys.argv[2])
    e = [int(i) for i in evidence if i != ' ']
    if len(e) != numSteps:
        print "Input Error: length of sequence should matchs numSteps!"
        exit()
        
    f = np.array([0.5, 0.5])
    for i in range(numSteps):
        f = forward(f, e[i])
    
    print "P(R_%d = T|u_1:%d) = %.4f" % (numSteps, numSteps, f[0])
    print "P(R_%d = F|u_1:%d) = %.4f" % (numSteps, numSteps, f[1])
    
    
