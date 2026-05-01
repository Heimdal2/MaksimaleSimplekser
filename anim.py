import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sp
import main as m
import background as bck
import itertools

def all_faces(simplex):
    faces = []
    for k in range(1, len(simplex)+1):
        faces += list(itertools.combinations(simplex, k))
    return faces

cloud = m.clouds[0]

filtration = m.D

keys = sorted(filtration.keys())

fig, ax = plt.subplots()

def draw_complex(simplices):
    ax.clear()

    # draw points
    xs = [point[0] for point in cloud]
    ys = [point[1] for point in cloud]
    ax.scatter(xs, ys, color='black')

    faces = set()
