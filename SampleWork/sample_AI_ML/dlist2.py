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
            return self.formula.values[0]
        return (eg.getValue(key) in self.formula.values()) ^ (not self.flag)


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

def selectTest(examples):
    """ 
    create a test that best meet our need
    a little bit tricky to do
    """
    
    

def DList_Learning(examples, NTests):
    if len(examples) == 0:
        # create test that always return 'F'
        test = Test(CellTest('F'))
        return DList(test)
    [test, subEgs] = selectTest(examples)
    if (test == None):
        return None
    dlist = DList(test)
    re_egs = [eg for eg in examples if eg not in subEgs]
    dlist.updateNext(DList_Learning(examples, re_egs))
    return dlist
        
        
