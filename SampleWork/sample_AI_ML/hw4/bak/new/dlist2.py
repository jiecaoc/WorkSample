from classes import *
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
        
        
