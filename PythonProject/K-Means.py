import math

data = [
    (185, 72),
    (170, 56),
    (168, 60),
    (179, 68),
    (182, 72),                                               
    (188, 77)
]

c1 = data[0]
c2 = data[1]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def mean(points):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return (round(x, 2), round(y, 2))

for iteration in range(2):
    cluster1 = []
    cluster2 = []

    for point in data:
        d1 = distance(point, c1)
        d2 = distance(point, c2)

        if d1 < d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    c1 = mean(cluster1)
    c2 = mean(cluster2)

    print(f"\nIteration {iteration+1}")
    print("Cluster 1:", cluster1)
    print("Cluster 2:", cluster2)
    print("New Centroid C1:", c1)
    print("New Centroid C2:", c2)
