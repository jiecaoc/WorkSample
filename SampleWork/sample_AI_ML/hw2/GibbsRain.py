import random 


# sampling according to p
def sampling(p):
    k = random.random()
    # print k
    if k < p:
        return True
    else:
        return False

    
def Gibbs_ask(N):  # N be the time of iteration
    # To simplify, label [C,R,S,W] as [0,1,2,3]
    # In our problem, S, W are given
    
    # the Bayesian Networks, Randomly initialize it
    bn = [True, False, True, True]
    # the non-evidence variables in bn
    Z = [0, 1]
    # n count of r, initially zero
   n = 0
    # do the sampling
    for j in range(1, N + 1):
    if bn[0]:
            bn[1] = sampling(0.814815);
        else:
            bn[1] = sampling(0.215686);

        if bn[1]:
            bn[0] = sampling(0.444444);
        else:
            bn[0] = sampling(0.047619);
        if bn[1]:
                n = n + 1
    return (n + 0.0) / N

    
if __name__ == '__main__':
    N = int(raw_input("Please input sumSteps : "))
    print "P(r|s,w) =", Gibbs_ask(N) 
   


