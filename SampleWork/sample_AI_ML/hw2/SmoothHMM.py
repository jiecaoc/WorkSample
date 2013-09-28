# Author: Jiecao Chen
# Email : Jieca001@umn.edu
# make sure you have install numpy to run this script
import numpy as np


# Transition Matrix
T = np.array([[.7, .3], [.4, .6]])
# Sensor matrix
E = np.array([[.9, .1], [.3, .7]])


# Normalize vec
def Normalize(vec):
    return vec / (vec.sum() + .0)

    
def Forward(fv, ev):
    return Normalize(E[:, 1 - ev] * np.dot(fv, T))

    
def Backward(bv, ev):
    return E[:, 1 - ev] * np.dot(T, bv)    
        
# initial distribution X0
X0 = np.array([0.5, 0.5])



    
def Forward_Backward(ev, n=10, prior=X0):
    # inputs:
    #    ev, a vector of evidence values for steps 1,2,..,t
    #    prior, the prior distribution on the initial state, P(X0)
    # PS: The first elements in ev is meaningless
    n = len(ev)
    # vector of forward messages
    fv = [0] * (n + 1)
    fv[0] = prior
    # vector of backward messages
    b = np.array([1] * 2)
    # vector of smoothed estimates
    sv = [0] * (n + 1)
    # Forward
    for i in range(1, n + 1):
        fv[i] = Forward(fv[i - 1], ev[i - 1])
    # Backward
    for i in range(n):
        sv[n - i] = Normalize(fv[n - i] * b)
        b = Backward(b, ev[n - i - 1])
    return sv

    
if __name__ == "__main__":
    n = int(raw_input("n = "))
    ev = list(raw_input("Input the evidence sequence:"))
    ev = [int(i) for i in ev if i != ' ']
    ans = Forward_Backward(ev)
    ans = [p[0] for p in ans[1:]]
    for i in range(1, len(ans) + 1):
        print "P(X_%d=T|e1:%d) = %.5f" % (i, len(ans), ans[i - 1])




              
