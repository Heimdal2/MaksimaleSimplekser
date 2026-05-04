import numpy as np
import background as bck
import matplotlib.pyplot as plt

N = 10
samples = 1
dicts = []
maximals = []
clouds = []

for sample in range(samples):
    lower, upper = -1,1
#    P = np.random.uniform(lower, upper, (N,2))
    P = np.random.normal(lower, upper, (N,2))
#    P = np.array([[(upper-lower)*np.cos(2*np.pi*k/N),(upper-lower)*np.sin(2*np.pi*k/N)] for k in range(N)]) # Sirkel
#    P = np.round(P) # Rutenett
    D = bck.Program(P)
    MaxSimp = {}
    MaxSimpL = []
    for key in D:
        MaxSimp[key] = len(D[key])
        MaxSimpL.append(len(D[key]))

    maximals.append(MaxSimp)
    clouds.append(P)

#for i in range(samples):
#    M = np.array(list(maximals[i].items()))
#    P = clouds[i]
#    print(M)
#
#    plt.plot(*M.T)
#    plt.scatter(*M.T)
#    plt.grid()
#    plt.show()
#
#    plt.scatter(*P.T)
#    plt.grid()
#    plt.show()
