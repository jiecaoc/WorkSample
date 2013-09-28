import sys
import random
import copy
import numpy as np
# in mdpdata.py, some useful functions are defined as well as
# the data of mdp_world
from mdpdata import *


def policy_evaluation(r, gamma, pi, U):
    """
    need to solve AU = b
    """
    # # modified policy evaluation
    # new_U = copy.deepcopy(U)
    # for s in S:
    #     if s in term_S:
    #         continue
    #     new_U[s] = r + gamma * sum_s_a(s, pi[s], U)
    # return new_U
    
    # map s -> integer, which is its position in S
    pos = {}
    i = 0
    for s in S:
        pos[s] = i
        i = i + 1

    # construct the coefficient matrix and vector b, 
    n = len(S)
    b = np.array([r] * n)
    A = np.zeros((n, n))

    # specify the value in A
    for s in S:
        if s in term_S:
            continue
        p = pos[s]
        A[p, p] = 1.
        a = pi[s]
        act = [a, neig[a][0], neig[a][1]]
        w = [0.8, 0.1, 0.1]
        for i in range(3):
            new_s = moveto(s, act[i])
            A[pos[s], pos[new_s]] = A[pos[s], pos[new_s]] - gamma * w[i]
    for s in term_S:
        p = pos[s]
        A[p, p] = 1
        b[p] = U[s]

    # solve Ax = b
    x = np.linalg.solve(A, b)
    new_U = {}
    for i in range(len(S)):
        new_U[S[i]] = x[i]
    return new_U




def policy_iteration(r):
    """
    algorithm follows AIMA_ed_3 -- 657
    """
    gamma = 0.9999999999999
    # initialize U and pi
    U = {}
    pi = {}
    for s in S:
        U[s] = 0
        pi[s] = random.choice(A)
    for s in term_S:
        pi[s] = 'N'
    U[(4, 3)] = 1
    U[(4, 2)] = -1
    while True:
        U = policy_evaluation(r, gamma, pi, U)
        unchanged = True
        for s in S:
            if s in term_S:
                continue
            [a, mvalue] = getMax(s, U)
            if mvalue > sum_s_a(s, pi[s], U):
                pi[s] = a
                unchanged = False
        if unchanged:
            break
    return[pi, U]

def main():
    if (len(sys.argv) == 2):
        r = float(sys.argv[1])
    else:
        print "Error: Missing r"
        exit()
    [pi, U] = policy_iteration(r)
    for s in S:
        print 's =', s, ': U[s] = %.4f'% (U[s],), ', a =', pi[s]


if __name__ == '__main__':
    main()
