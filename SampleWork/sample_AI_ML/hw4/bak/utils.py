# some common functions and varibles that will be 
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
