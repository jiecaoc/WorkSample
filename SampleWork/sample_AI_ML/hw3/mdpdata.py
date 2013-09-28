#!/usr/bin/python
# Filename: mdpdate.py

# the set of all states
S = []
for x in range(4):
    for y in range(3):
        S.append((x + 1, y + 1))
S.remove((2,2))
# set of terminal states
term_S = [(4, 2), (4, 3)]
# action set
move = {'u': (0, 1), 'd': (0, -1), 'l': (-1, 0), 'r': (1, 0)}
A = ['u', 'd', 'l', 'r']
# action neighbor
neig = {'u': ('l', 'r'), 'd': ('r', 'l'), 'l': ('d', 'u'), 'r': ('u', 'd')}



def moveto(s, a):
    """start from s, take action a"""
    new_s = (s[0] + move[a][0], s[1] + move[a][1])
    if new_s in S:
        return new_s
    else:
        return s

def sum_s_a(s, a, U):
    """ calculate \sum_{s'} P(s'|s,a) U[s']"""
    if s in term_S:
        return U[s]
    value = 0
    act = [a, neig[a][0], neig[a][1]]
    w = [0.8, 0.1, 0.1]
    for i in range(3):
        new_s = moveto(s, act[i])
        value = value + w[i] * U[new_s]
    return value
        

def getMax(s, U):
    """
    calculate \max_{a \in A(s)} \sum_{s'} P(s'|s,a) U[s']
    input s -- state
    outputs: a -- optimal action
             mvalue -- max value
    """
    if s in term_S:
        return ['N', U[s]]
    mvalue = -10000000
    optimal_a = 'u'
    for a in A:
        value = sum_s_a(s, a, U)
        if (mvalue < value):
            optimal_a = a
            mvalue = value
            
    return [optimal_a, mvalue]
