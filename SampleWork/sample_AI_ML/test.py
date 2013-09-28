from dlist2 import CellTest, Test
from utils import *
from classes import *
# class Test:
#     def __init__(self, v):
#         self.value = v
#     def test(self, v):
#         return self.value + v

# f = lambda x: x.test(1)
# ls = [Test(1), Test(2), Test(4)]
# print map(f, ls)

examples = importData('dataset.csv')
A = Attribute('Alt')
A.addValue('T')
ctest1 = CellTest(A)
A = Attribute('Bar')
A.addValue('T')
ct2 = CellTest(A)
T = Test(ctest1)
T.addCTest(ct2)
for eg in examples:
    print eg
    print T.test(eg)

