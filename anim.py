import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sp
import main as m
import background as bck
import itertools
from matplotlib.animation import FuncAnimation


def all_faces(simplex):
    faces = []
    for k in range(1, len(simplex)+1):
        faces += list(itertools.combinations(simplex, k))
    return faces

cloud = m.clouds[0]

filtration = m.D

keys = sorted(filtration.keys())

M = np.array(list(m.maximals[0].items()))
M_ = np.array([p[1] for p in M])

N = len(M_)


plt.scatter(range(len(M_)),M_)
plt.plot(range(len(M_)),M_)
plt.grid()
plt.title("Stegvis")
plt.show()

#plt.scatter(range(len(M_)),np.log(M_))
#plt.plot(range(len(M_)),np.log(M_))
#plt.grid()
#plt.title("Log-Stegvis")
#plt.show()

plt.scatter(*M.T)
plt.plot(*M.T)
plt.grid()
plt.title("Tidvis")
plt.show()

#X = np.array([p[0] for p in M])
#Y = np.array([np.log(p[1]) for p in M])
#
#plt.scatter(X,Y)
#plt.plot(X,Y)
#plt.grid()
#plt.title("Log-Tidvis")
#plt.show()

fig, ax = plt.subplots()

#def draw_complex(simplices):
#    ax.clear()
#
#    # draw points
#    xs = [point[0] for point in cloud]
#    ys = [point[1] for point in cloud]
#    ax.scatter(xs, ys, color='black')
#
#    faces = set()
#    for s in simplices:
#        faces.update(all_faces(s))
#
#    # edges
#    for f in faces:
#        if len(f) == 2:
#            x = [cloud[i][0] for i in f]
#            y = [cloud[i][1] for i in f]
#            ax.plot(x, y, color='blue')
#
#    # triangles
#    for f in faces:
#        if len(f) == 3:
#            x = [cloud[i][0] for i in f] + [cloud[f[0]][0]]
#            y = [cloud[i][1] for i in f] + [cloud[f[0]][1]]
#            ax.fill(x,y,alpha=0.3,color='orange')
#
#    ax.set_title('Filtration step')

def draw_simplex(simplex):
    simplex = sorted(simplex)
    
    if len(simplex) == 2:
        # edge
        p = cloud[simplex]
        ax.plot(p[:, 0], p[:, 1], color='blue')
        
    elif len(simplex) == 3:
        # triangle
        p = cloud[simplex]
        polygon = plt.Polygon(p, alpha=0.3, color='blue')
        ax.add_patch(polygon)
        
    elif len(simplex) > 3:
        # draw all 2-faces (projection approach)
        from itertools import combinations
        for face in combinations(simplex, 3):
            p = cloud[list(face)]
            polygon = plt.Polygon(p, alpha=0.1, color='blue')
            ax.add_patch(polygon)

def update(frame):
    ax.clear()
    
    # redraw points
    ax.scatter(cloud[:, 0], cloud[:, 1], color='black')
    
    t = keys[frame]
    simplices = filtration[t]
    
    for simplex in simplices:
        draw_simplex(simplex)
    
    ax.set_title(f"Filtration value = {t:.2f}")
    ax.set_aspect('equal')
    ax.grid()

ani = FuncAnimation(fig, update, frames=len(keys), interval=800)
plt.show()
