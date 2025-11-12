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
def dist(a,b):
    ax, ay = points[a]; bx, by = points[b]
    return math.hypot(ax-bx, ay-by)
d = { (i,j): dist(i,j) for i in I for j in J }
best_R = float('inf')
best_S = None
best_assign = None
for S in itertools.combinations(J, p):
    assign = {}
    worst = 0.0
    for i in I:
        nearest = min((d[(i,j)], j) for j in S)
        assign[i] = nearest[1]
        worst = max(worst, nearest[0])
    if worst < best_R:
        best_R = worst
        best_S = S
        best_assign = assign
print("Best sites:", best_S)
print("Worst distance R:", round(best_R, 3))
print("Assignments:", best_assign)
