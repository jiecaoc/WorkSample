# It's a general framework of Bakc-prop-network
# by Jiecao Chen (jieca001@umn.edu)
# follow the idea in AIMA - page 734
# maybe, if I want to make the algorithm more efficient,
# I should use numpy
from utils import *
import math
import random
def g(x):
    return 1.0 / (1 + math.exp(-x))

def dg(x):
    # if didn't do this, NN converge very slow
    x = x / 100
    return math.exp(-x) / (1 + math.exp(-x)) * (1 + math.exp(-x))

def norm(a, b):
    nm = 0
    for i in range(len(a)):
        nm = nm + abs(a[i] - b[i])
    return nm



class BPNN:
    """
    BP-Neural Network,
    eg:
       # create a network with #inputs=4, #outputs=2
       net = BPNN((4,5,25,2))
       net.train(examples)
       print net.classify(eg)
    """
    
    def __init__(self, dimention_vec, eps=0.5, alpha = 0.1):
        """ 
        eg: dimention_vec = (3,5,7,2)
            3 will be #input layer
            2 will be #output layer
        """
        self.eps = eps
        self.alpha = alpha
        self.layers = []
        self.dimention_vec = dimention_vec
        # to save memory, use dict represents the weight
        self.w = {}
        n = 0
        for clay in dimention_vec:
            tmp = range(clay)
            tmp = map(lambda x: x+n, tmp)
            n = n + clay
            self.layers.append(tmp)
        #print self.layers
        # a vector of errors
        self.deltas = range(sum(dimention_vec))

            
    def train(self, examples):
        """ given examples, train the BPNN """
        # initialize the weights
        for i in range(len(self.layers) - 1):
            a = self.layers[i]
            b = self.layers[i+1]
            for j in a:
                for k in b:
                    self.w[(j,k)] = random.random()        
        # each eg should has self.dimention (#inputs + #outputs)
        # eg = (inputs, outputs)
        # eg should be vector of numbers
        while True:
            for eg in examples:
#                print "now: ", eg
                [a, into] = self.propagateFwd(eg)
                # Propagate deltas backward from output layer to input layer
                outputs = self.layers[len(self.layers) - 1]
                for j in outputs:
                    self.deltas[j] = dg(into[j]) * (eg[j] - a[j])
#                print self.deltas[1]
                for l in range(len(self.layers) - 1):
                    for i in self.layers[len(self.layers) - 2 - l]:
                        x = self.layers[len(self.layers) - 1 - l]
                        x = map(lambda j: self.w[(i,j)] * self.deltas[j], x)
                        self.deltas[i] = dg(into[i]) * sum(x)
                # Update every weight in network using deltas 
                for key in self.w.keys():
                    self.w[key] = self.w[key] + self.alpha \
                                  * a[key[0]] * self.deltas[key[1]]
            if self.loss(examples) < self.eps:
                break
    
    def propagateFwd(self, eg):
        """ Propagate the inputs forward to compute the outputs """
        a = range(sum(self.dimention_vec))
        into = range(sum(self.dimention_vec))
        inputs = self.layers[0]
        for i in inputs:
            a[i] = eg[i]
        for l in range(len(self.layers) - 1):
            for j in self.layers[l + 1]:
                x = self.layers[l]
                x = map(lambda i: self.w[(i,j)] * a[i], x)
                into[j] = sum(x)
                a[j] = g(into[j])
        return [a, into]
    
    def classify(self, eg):
        """ given an eg vector, return it's classification """
        [a, into] = self.propagateFwd(eg)
        outputs = self.layers[len(self.layers) - 1]
        return [a[i] for i in outputs]
    
    def loss(self, examples):
        """ evaluate the loss of the NN """
        ls = 0
        cd = len(self.dimention_vec)
        pos = sum(self.dimention_vec) - self.dimention_vec[cd-1]
        for eg in examples:
            [a, into] = self.propagateFwd(eg)
            ls = ls + norm(a[pos:], eg[pos:])
        return ls


def Hash(x):
    h = hash(x)
    if h > 0:
        x = (h + 0.0) / hash('F')
        if x == 1:
            return 0
        else:
            return x
    else:
        return (h + 0.0) / hash('T')

def classify(x):
    if x[0] > 0.5:
        return 'T'
    else:
        return 'F'

#=========== main ==============
if __name__ == '__main__':        
    examples = importData('dataset.csv')
    
    f = lambda eg: [Hash(eg.getValue(key)) for key in attris]
    new_examples = map(f, examples)

    #for eg in examples:
    #   print eg
    # create new BPNN, set eps = 0.5
    NN = BPNN((10, 1), .5)
    # train the BPNN by data
    NN.train(new_examples)
    
    ct = 0
    for i in range(len(examples)):
        trueCls = examples[i].getValue('classification')
        nnCls = classify(NN.classify(new_examples[i]))
        if trueCls == nnCls:
            ct = ct + 1
        print "Example", i, "True class:",trueCls,\
            ", classified by NN:", nnCls
    print "training dataset error rate:", 1 - (ct + 0.0) / len(examples)


    print "\nNow do LOOCV ..."
    i = 0
    ct = 0
    for i in range(len(new_examples)):
        data = [new_examples[j] for j in range(len(new_examples)) if j != i]
        NN = BPNN((10, 1))
        NN.train(data)
        trueCls = examples[i].getValue('classification')
        nnCls = classify(NN.classify(new_examples[i]))
        if trueCls == nnCls:
            ct = ct + 1
        print "Example", i, "True class:",trueCls,\
            ", classified by NN (leave Example", i, "out):", nnCls
    print "LOOCV error rate:", 1 - (ct + 0.0) / len(examples)
