
import numpy as np
import utilities as ut

def sigma(x):
    if x > 30:
        x = 30
    if x < -30:
        x = -30
    #print x
    return 1 / (1 + np.exp(-x))

def Pi(w, phi):
    tmp = np.dot(phi, w).transpose().tolist()[0]
    return ut.ls2Vec(map(sigma, tmp))
    
def calcR(pi):
    tmp = [pi[n, 0] * (1 - pi[n, 0]) for n in range(len(phi))]
    return np.diag(tmp)

def calculateW(phi, y):
    w0 = ut.ls2Vec([1] * phi.shape[1])
    w1 = ut.ls2Vec([0.5] * phi.shape[1])
    delta = 1
    while delta > 0.5:
        w0 = w1
        pi = Pi(w0, phi)
        R = calcR(pi)
        tmp = reduce(np.dot, [phi.transpose(), R, phi])
        z = np.dot(phi, w0) - np.dot(np.linalg.inv(R), (pi - y))
        w1 = reduce(np.dot, [np.linalg.inv(tmp), phi.transpose(), R, z])
        delta = np.linalg.norm(np.dot(phi.transpose(), (y - pi)))
        print delta
    return w1
       
    
# import data

data = ut.importRawData('Pima.csv')
k = 100
y = ut.ls2Vec(map(lambda x: x[0] - 1 , data[1:k]))

phi = np.array(map(lambda x: x[1:], data[1:k]))
#print phi
w = calculateW(phi, y)
#print calcR(Pi(w, phi))
#pi = Pi(w, phi)
#print np.linalg.det(np.dot(phi.transpose(), phi))
# w = reduce(np.dot, [np.linalg.inv(np.dot(phi.transpose(), phi)) , phi.transpose(), y])
print w
for x in data[1:k]:
   print x[0] - 1, sigma( np.dot(w.transpose(), ut.ls2Vec(x[1:])))
#print np.dot(phi.transpose(), (y - pi))