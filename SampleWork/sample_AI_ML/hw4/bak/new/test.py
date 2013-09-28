from utils import *

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
