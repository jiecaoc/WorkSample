import sys
import copy
from mdpdata import *



    
def value_iteration(r, epsilon):
    """
    using value iteration algorithm
    to decide utilities and optimal policy.
    
    inputs: epsilon -- max error allowed in the utility of any state
    outputs: pi -- optimal policy
             U -- utility
    """
    # optimal policy
    pi = {}
    gamma = 0.999999999999
    delta = epsilon * (1 - gamma) / gamma
    U = {}
    for s in S:
        U[s] = 0
    U[(4, 3)] = 1
    U[(4, 2)] = -1
    last_U = copy.deepcopy(U)
        
    while True:
        last_U = copy.deepcopy(U)
        d = 0
        for s in S:
            # do not calculate states in term_S
            if s in term_S:
                pi[s] = 'N'
                continue
            # get max value and optimal action    
            [pi[s], mvalue] = getMax(s, last_U)
            U[s] = r + gamma * mvalue
            if abs(U[s] - last_U[s]) > d:
                d = abs(U[s] - last_U[s])
        if (d < delta):
            break
    return [pi, U]


def outputDiagram(pi, U):
    """
    print the state diagram of the result
    """
    for y in [3, 2, 1]:
        print y, ': ',
        for x in [1, 2, 3, 4]:
            s = (x,y)
            if s == (2, 2):
                print "          |",
            else:
                print pi[s], "%.4f  |" % (U[s],),
        print '\n'


def main():
    if (len(sys.argv) == 2):
        r = float(sys.argv[1])
    else:
        print "Error: Missing r"
        exit()
    [pi, U] = value_iteration(r, 0.01)
    for s in S:
        print 's =', s, ': U[s] = %.4f'% (U[s],), ', a =', pi[s]
    # outputDiagram(pi, U)

    
if __name__ == "__main__":
    main()
