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

def diam(sigma,M):
    return np.max(M[sigma][:,sigma])

def eliminer_delmengder(S):
    S_ = sorted(S, key=len, reverse=True)
    res = []
    for A in S_:
        if not np.any(np.array([isSubset(A,B) for B in res])):
            print(A)
            res.append(A)

    return res

def P(S):
    return [list(c) for r in range(3,len(S)+1) for c in combinations(range(len(S)),r)]

def Diametre(S):
    S_ = P(S)


print(Maksimale(P(range(N))))
