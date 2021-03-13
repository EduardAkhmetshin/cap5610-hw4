import numpy as np
from scipy import spatial

a = [
    [4.7, 3.2],
    [4.9, 3.1],
    [5.0, 3.0],
    [4.6, 2.9]
]

b = [
    [5.9, 3.2],
    [6.7, 3.1],
    [6.0, 3.0],
    [6.2, 2.8]
]

distances = []
for point_a in a:
    for point_b in b:
        distances.append(spatial.distance.euclidean(point_a, point_b))

distances.sort()
print(distances)
print(np.mean(distances))
