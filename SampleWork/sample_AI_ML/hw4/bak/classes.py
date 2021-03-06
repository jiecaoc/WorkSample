dlist2.py                                                                                           0000664 0001750 0001750 00000007426 12135554230 010724  0                                                                                                    ustar   cjc                             cjc                                                                                                                                                                                                                    from classes import *
from utils import *
class CellTest:
    """
    CellTest test only one attribute,
    eg: ctest = CellTest(A) only test whether
        an example, say eg's value of A attr is in A's values set 
        A is an instance of class Attribute
    """
    def __init__(self, att, flag=True):
        # if att is a string
        # test always return the value att
        if type(att) == type('ss'):
            A = Attribute('const')
            A.addValue(att)
            att = A
        self.flag = flag
        self.formula = att
        
    def test(self, eg):
        key = self.formula.key()
        if key == 'const':
            return True
        return (eg.getValue(key) in self.formula.values()) ^ (not self.flag)

    def __str__(self):
        return self.formula.key() + " " + reduce(lambda x,y: x+y, self.formula.values())

class Test:
    """
    the test is represented as
        (!flag) ^ (ct1 /\ ct2 /\ ct3 /\ ... /\ ctn)
    in principle, it can represent any test
    """
    def __init__(self, ctest, flag=True):
        self.ctestList = []
        self.ctestList.append(ctest)
        self.flag = flag

    def addCTest(self, ctest):
        self.ctestList.append(ctest)

    def test(self, eg):
        f = lambda ctest: ctest.test(eg)
        ans = map(f, self.ctestList)
        f = lambda x, y: x & y
        ans = reduce(f, ans)
        if self.flag:
            return ans
        else:
            return not ans
    def __str__(self):
        ls = map(lambda x: x.__str__() + ", ", self.ctestList)
        return reduce(lambda x,y: x + y, ls)

class DList:
    def __init__(self, test, classification):
        self.test = test
        self.next = None
        # classification when test return True
        self.classification = classification
        
    def updateNext(self, dlist):
        self.next = dlist
        
    def makeDecision(self, eg):
        if self.test(eg):
            return self.classification
        else:
            dlist = self.next
            return dlist.makeDecision(eg)
    def show(self):
        """ print the DList """
        print self.test, "==>", self.classification, ", otherwise"
        if self.next:
            self.next.show()

def selectTest(attris, examples):
    """ 
    create a test that best meet our need
    a little bit tricky to do
    """
    if len(attris) == 1:
        # can't find a legal test
        return 'Failed!'
    A = argmax_importance(attris, examples, examples)
    f = lambda v: [eg.getValue('classification') for eg in examples 
                   if eg.getValue(A.key()) == v]
    TFLists = map(f, A.values())
    ls = map(countTF, TFLists)
    ls = map(lambda x: (x[0]+0.0)/sum(x), ls)
    ls = map(B, ls)
    m = min(ls)
    record = 0
    for i in range(len(ls)):
        if ls[i] == m:
            record = i
            break
    key = A.key()
    v = A.values()[record]
    A.clearValues()
    A.addValue(v)
    # if is fully classified,
    if m == 0:
        # return [class, ctest]
        return [TFLists[record][0], CellTest(A)]
    egs = [eg for eg in examples if eg.getValue(key) == v]
    newatts = [att for att in attris if att != key]
    test = selectTest(newatts, egs, egs)
    return [test[0], CellTest(A)].extend(test[1:])
    

def DList_Learning(examples, NTests=4):
    if len(examples) == 0:
        # create test that always return 'F'
        test = Test(CellTest('F'))
        return DList(test, 'F')
    class_ctests = selectTest(attris, examples)
    classification = class_ctests[0]
    
    test =  Test(class_ctests[1])
    for ct in class_ctests[2:]:
        test.addCTest(ct)
    if (test == None):
        return None
    dlist = DList(test, classification)
    re_egs = [eg for eg in examples if not test.test(eg)]
    dlist.updateNext(DList_Learning(re_egs))
    return dlist
        
        
                                                                                                                                                                                                                                          dtree4.py                                                                                           0000664 0001750 0001750 00000007415 12135547732 010721  0                                                                                                    ustar   cjc                             cjc                                                                                                                                                                                                                    import math
from classes import *
from sets import Set
from utils import *
globalExamples = []


def PluralityValue(egs):
    """
    return the most common classification in egs
    """
    values = [eg.getValue('classification')
             for eg in egs]
    d = {}
    for v in values:
        d[v] = 0
    for v in values:
        d[v] = d[v] + 1
    m = max(d.values())
    if m * 2 == len(values):
        return 'T'
    for v in values:
        if d[v] == m:
            return v


    
        
def DTree_Learning(examples, attris, parent_examples, depth):    
    """
    Learn the decision tree, under the depth limit
    """
    # test whether examples are empty
    if len(examples) == 0:
        A = Attribute('classification')
        A.addValue(PluralityValue(parent_examples))
        return Tree(A)

    # test whether all classifications are same
    classifications = Set([eg.getValue('classification') 
                           for eg in examples])
    if len(classifications) == 1:
        A = Attribute('classification')
        for v in classifications:
            A.addValue(v)
        return Tree(A)

    # test whether attris are empty, note 'classification' always exists
    if len(attris) == 1:
        A = Attribute('classification')
        A.addValue(PluralityValue(examples))
        return Tree(A)
    
    # if exceed the depth limit
    if depth == 0:
        A = Attribute('classification')
        A.addValue(PluralityValue(examples))
        return Tree(A)
        
    
    # regular work                    
    A = argmax_importance(attris, examples, globalExamples)
    
    # create a new tree with root A
    tree = Tree(A)
    newAttris = [a for a in attris]
    newAttris.remove(A.key())
#    print A.key()
#    print A.values()
#    print ' =============== '
    for v in A.values():
        exs = [e for e in examples if e.getValue(A.key()) == v]
        subtree = DTree_Learning(exs, newAttris, examples, depth - 1)
        tree.addChild(v, subtree)
    return tree


            

def printTree(tree):
    """
    print the Desition Tree in a readable way
    """
 #   print tree
    if tree.getAttr() == 'classification':
        print tree.getClassValue()
        return 
    print tree, '\'s children =============='
    Children = tree.getChildrenList()
#    print Children
    for item in Children:
        if item[1].getAttr() != 'classification':
            print item[0], item[1]
        else:
            print item[0], item[1].getClassValue()
    for item in Children:
        if item[1].getAttr() != 'classification':
            printTree(item[1])

def ErrorLOOCV(examples, attris):
    errorCount = 0
    for i in range(len(examples)):
        tmp = [eg for eg in examples]
        tmp.remove(examples[i])
        tree = DTree_Learning(tmp, attris, tmp, 5)
        a = examples[i].getValue('classification')
        b = tree.makeDecision(examples[i])
        print 'leave Example', i+1, 'out:','real class -', a, ',by DTree -', b
        if a != b: 
            errorCount = errorCount + 1
    return (errorCount + 0.0) / len(examples)





#=================main ===============

examples = importData('dataset.csv')
globalExamples = examples
#=====Training set error rate===============
tree = DTree_Learning(examples, attris, examples, 4)
print "The tree structure after learning from all example:"
printTree(tree)
errorCount = 0
for i in range(len(examples)):
    a = tree.makeDecision(examples[i])
    b = examples[i].getValue('classification')
    if a != b:
        errorCount = errorCount + 1
print "Training Set Error Rate:", (errorCount + 0.0) / len(examples)
print '\n'
#======LOOCV error rate======================
print "Now do LOOCV :"
tree = DTree_Learning(examples, attris, examples, 4)
errorRate = ErrorLOOCV(examples, attris)
print 'LOOCV Error Rate:', errorRate


                                                                                                                                                                                                                                                   perceptron.py                                                                                       0000664 0001750 0001750 00000006115 12135643564 011707  0                                                                                                    ustar   cjc                             cjc                                                                                                                                                                                                                    # It's a general framework of Bakc-prop-network
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                   test.py                                                                                             0000664 0001750 0001750 00000002007 12135645473 010502  0                                                                                                    ustar   cjc                             cjc                                                                                                                                                                                                                    from utils import *

# class Test:
#     def __init__(self, v):
#         self.value = v
#     def test(self, v):
#         return self.value + v

# f = lambda x: x.test(1)
# ls = [Test(1), Test(2), Test(4)]
# print map(f, ls)

#examples = importData('dataset.csv')
# A = Attribute('Alt')
# A.addValue('T')
# A.addValue('F')
# ctest1 = CellTest(A)
# print ctest1
# A = Attribute('Bar')
# A.addValue('T')
# ct2 = CellTest(A)
# print ct2
# T = Test(ctest1)
# T.addCTest(ct2)
# print T

#dlist = DList_Learning(examples) 
#dlist.show()

# key = 'Pat'
# attris.remove(key)
# egs = [eg for eg in examples if eg.getValue(key) != 'Some']
# key = 'Hun'
# attris.remove(key)
# egs = [eg for eg in egs if eg.getValue(key) != 'F']
# for e in egs:
#     print e
# test = selectTest(attris, egs)
# for x in test:
#     print x
# for eg in examples:
#     print eg
#     print T.test(eg)

examples = importData('dataset.csv')
f = lambda eg: [hash(eg.getValue(key)) for key in attris]
examples = map(f, examples)
for eg in examples:
    print eg
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         utils.py                                                                                            0000664 0001750 0001750 00000004413 12135536344 010662  0                                                                                                    ustar   cjc                             cjc                                                                                                                                                                                                                    # some common functions and varibles that will be 
# shared in different program
import csv
import math
from classes import *
attris = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est', 'classification']

def importData(file):
    """
    create examples from csv format file
    input: file name
    output: examples
    """
    with open(file,'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter = ',', quotechar='|')
        examples = []
	for row in datareader:
            pairs = []
            for i in range(len(row)):
                row[i] = row[i].replace(" ","")
                pairs.append((attris[i], row[i]))
            examples.append(Example(pairs))
    #globalExamples = examples
    return examples

def countTF(ls):
    """ 
    input: a list, element in {T,F},
    output: (#T, #F)
    """
    all = len(ls)
    ct = 0
    for x in ls:
        if x == 'T':
            ct = ct + 1
    return (ct, all - ct)

def B(p):
    """ entropy of Boolean r.v."""
    if (p == 0 or p == 1):
        return 0
    return -(p * math.log(p) + (1 - p) * math.log(1 - p))

def GainInfo(a, egs):
    """
    calc Gain(a) = B(p/(p+n)) - Remainder(a)
    see AIMA page 704
    """
    
    dic = {}
    for eg in egs:
        v = eg.getValue(a)
        dic[v] = []
    for eg in egs:
        v = eg.getValue(a)
        dic[v].append(eg.getValue('classification'))
#    print dic
    
    ls = map(countTF, dic.values())
#    print ls
    f = lambda x, y: (x[0] + y[0], x[1] + y[1])
    tot = reduce(f, ls)
#    print tot
    remainder = 0
    for x in ls:
        remainder = remainder + (sum(x)+ 0.0) / sum(tot) \
                    * B((x[0] + 0.0) / sum(x))

    return B((tot[0] + .0) / sum(tot)) - remainder


def argmax_importance(attris, examples, globalExamples):
    """
    return the most important attribute in attris,
    use the entropy method
    """
    GainInfos = [ GainInfo(a, examples) for a in attris if a != 'classification']
    m = max(GainInfos)
    for i in range(len(attris) - 1):
        if GainInfos[i] == m:
            key = attris[i]
            break
    A = Attribute(key)
    values = []
    for eg in globalExamples:
        v = eg.getValue(key)
        if v not in values:
            values.append(v)
            A.addValue(v)
    return A
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     