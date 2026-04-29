import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as sp
from itertools import combinations

#fig = plt.figure()
#ax = fig.add_subplot(111)
#
#N = 15
#np.random.seed(100)
#P = np.random.uniform(0, 10, (N,2))
#P = np.round(P)
#
## P = np.array([[np.cos(2*np.pi*k/N), np.sin(2*np.pi*k/N)] for k in range(N)])
#
#M = sp.cdist(P,P,'euclidean')
#print(type(P))

def isSubset(A,B):
    return np.all(np.isin(A,B))

def diam(sigma,M,r=2):
    return np.round(np.max(M[sigma][:,sigma]),r)

def eliminer_delmengder(S):
    S_ = sorted(S, key=len, reverse=True)
    res = []
    for A in S_:
        if not np.any(np.array([isSubset(A,B) for B in res])):
            res.append(A)

    return res

def Power(S):
    return [list(c) for r in range(2,len(S)+1) for c in combinations(S,r)]

def Diametre(S, M):
    diams = {}
    for sigma in Power(S):
        diams[tuple(sigma)] = diam(sigma,M,r=2)

    return diams

#Diams = Diametre(range(N), M)
#Filt = {}
#
#for value in Diams.values():
#    Simplekser = [list(k) for k, v in Diams.items() if v <= value]
#    Filt[value] = eliminer_delmengder(Simplekser)
#
#Filt = {k: v for k, v in sorted(Filt.items(), key=lambda
#    item: item[0])}
#
#for key in Filt:
#    print(key, Filt[key])
#    print(" ")


def Program(P,M=None):
    N = len(P)
    if M == None:
        M = sp.cdist(P,P,'euclidean')
    
    Diams = Diametre(range(N), M)
    Filt = {}

    for value in Diams.values():
        Simplekser = [list(k) for k, v in Diams.items() if v <= value]
        Filt[value] = eliminer_delmengder(Simplekser)
    
    Filt = {k: v for k, v in sorted(Filt.items(), key=lambda item: item[0])}
    
    return Filt

