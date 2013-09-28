# It's a general framework of Bakc-prop-network
# by Jiecao Chen (jieca001@umn.edu)
# follow the idea in AIMA - page 734
from utils import *
import random

class BPNN:
    def __init__(self, dimention_vec):
        """ 
        eg: dimention_vec = (3,5,7,2)
            3 will be #input layer
            2 will be #output layer
        """
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

        # initialize the weights
        for i in range(len(dimention_vec) - 1):
            a = self.layers[i]
            b = self.layers[i+1]
            for j in a:
                for k in b:
                    self.w[(j,k)] = random.random()
        # a vector of errors
        self.delta = range(sum(dimention_vec))

            
    def train(self, examples):
        # NN output of each node
        a = range(sum(self.dimention_vec))
        into = range(sum(self.dimention_vec))
        # each eg should has self.dimention (#inputs + #outputs)
        # eg = (inputs, outputs
        # eg should be vector of numbers
        iterCount = 0
        while True:
            for eg in examples:
                [a, into] = self.propagateFwd(eg)
                # Propagate deltas backward from output layer to input layer
                outputs = self.layers[len(self.layers)]
                for j in outputs:
                    self.deltas[j] = dg(into[j]) * (eg[j] - a[j])
                for l in range(len(self.layers) - 1):
                    for i in self.layers[len(self.layers) - 1 - l]:
                        x = self.layers[len(self.layers) - l]
                        x = map(lambda j: self.w[(i,j)] * self.deltas[j], x)
                        self.deltas[i] = g(into[i]) * sum(x)
                # Update every weight in network using deltas 
                for key in self.w.keys():
                    self.w[key] = self.w[key] + alpha \
                                  * a[key[0]] * self.deltas[key[1]]
            if iterCount > 100:
                break
            else:
                iterCount = iterCount + 1
    
    def propagateFwd(self, eg):
        # Propagate the inputs forward to compute the outputs 
        a = range(sum(self.dimention_vec))
        into = range(sum(self.dimention_vec))
        inputs = self.layers[0]
        for i in inputs:
            a[i] = eg[i]
            for l in range(len(self.layers) - 1):
                for j in self.layers[l + 1]:
                    x = self.layers[l]
                    x = map(lambda i: self.w[(i,j)] * a[i]), x)
                    into[j] = sum(x)
                    a[j] = g(into[j])
        return [a, into]
    
    def classify(self, eg):
        """ given an eg vector, return it's classification """
        [a, into] = self.propagateFwd(eg)
        outputs = self.layers[len(self.layers)]
        return [a[i] for i in outputs]

#=========== main ==============
