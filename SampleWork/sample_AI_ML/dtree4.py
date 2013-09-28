import math
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


def GainInfo(a, egs):
    """
    calc Gain(a) = B(p/(p+n)) - Remainder(a)
    see AIMA page 704
    """
    # entropy of Boolean r.v.
    def B(p):
        if (p == 0 or p == 1):
            return 0
        return -(p * math.log(p) + (1 - p) * math.log(1 - p))
    dic = {}
    for eg in egs:
        v = eg.getValue(a)
        dic[v] = []
    for eg in egs:
        v = eg.getValue(a)
        dic[v].append(eg.getValue('classification'))
#    print dic
    def countT(ls):
        all = len(ls)
        ct = 0
        for x in ls:
            if x == 'T':
                ct = ct + 1
        return (ct, all - ct)
    ls = map(countT, dic.values())
#    print ls
    f = lambda x, y: (x[0] + y[0], x[1] + y[1])
    tot = reduce(f, ls)
#    print tot
    remainder = 0
    for x in ls:
        remainder = remainder + (sum(x)+ 0.0) / sum(tot) \
                    * B((x[0] + 0.0) / sum(x))

    return B((tot[0] + .0) / sum(tot)) - remainder


def argmax_importance(attris, examples):
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
    A = argmax_importance(attris, examples)
    
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

