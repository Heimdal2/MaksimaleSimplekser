import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as sp
from itertools import combinations


N = 5
np.random.seed(69)
P = np.random.uniform(0, 10, (N,2))
M = sp.cdist(P,P,'euclidean')


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

def P(S):
    return [list(c) for r in range(2,len(S)+1) for c in combinations(S,r)]

def Diametre(S, M):
    diams = {}
    for sigma in P(S):
        diams[tuple(sigma)] = diam(sigma,M)

    return diams

Diams = Diametre(range(N), M)
Filt = {}

for value in Diams.values():
    Simplekser = [list(k) for k, v in Diams.items() if v <= value]
    Filt[value] = eliminer_delmengder(Simplekser)


for key in Filt:
    print(key, Filt[key])
    print(" ")
