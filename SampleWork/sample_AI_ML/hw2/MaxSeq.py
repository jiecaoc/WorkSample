# Author : Jiecao Chen
# Email  : jieca001@umn.edu
# make sure you have install numpy to run this code
import numpy as np


# Transition Matrix
T = np.array([[.7, .3], [.4, .6]])
# Sensor matrix
E = np.array([[.9, .1], [.3, .7]])

T = np.array([[.7, .3], [.4, .6]])


# Normalize vec
def Normalize(vec):
    return vec / (vec.sum() + .0)

    
    
def MaxSeq(ev):
    ev = map(lambda x: 1 - x, ev)
    n = len(ev)
    # initial, when t = 1, mv = P(X1|e1)
    mv = np.array(E[:, ev[0]])
    # link states, indicate where the current state from
    preState = [[0] * 2 for x in range(n)]
    g = lambda arr: 1 if arr[1] > arr[0] else 0
    # forward
    for i in range(1, n):
        temp = (T.transpose() * mv).transpose()
        preState[i][0] = g(temp[:, 0])
        preState[i][1] = g(temp[:, 1])
        mv = Normalize(E[:, ev[i]] * temp.max(axis=0))
    t = g(mv)
    X = []
    for i in range(n):
        X.append(t)
        t = preState[n - i - 1][t]
    X.reverse()
    return [1 - x for x in X]    

    
if __name__ == "__main__":
    n = int(raw_input("n = "))
    ev = list(raw_input("Input the evidence sequence:"))
    ev = [int(i) for i in ev if i != ' ']

    print MaxSeq(ev)

