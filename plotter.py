import numpy as np
import matplotlib.pyplot as plt
import main as m

clouds = m.clouds
N = len(clouds)
M = []

for i in range(N):
    P = list(m.maximals[i].items())
    M_ = [p[1] for p in P]
    M.append(max(M_))

M = np.array(M)

print(M)

plt.scatter(range(N),M)
plt.plot(range(N),M)
plt.grid()
plt.show()
