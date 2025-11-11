import itertools, math

points = {
    "A": (0,0),
    "B": (0,4),
    "C": (3,0),
    "D": (6,4),
}

I = list(points.keys())
J = list(points.keys())
p = 2

def dist(a, b):
    ax, ay = points[a]; bx, by = points[b]
    return math.hypot(ax - bx, ay - by)

d = { (i,j): dist(i,j) for i in I for j in J }

best_R = float('inf')
best_S = None

for S in itertools.combinations(J, p):
    worst = max(min(d[(i,j)] for j in S) for i in I)
    if worst < best_R:
        best_R = worst
        best_S = S

print("Лучшие станции:", best_S)
print("Макс. расстояние R:", round(best_R, 3))
