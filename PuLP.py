import pulp as pl, math

coords = {"A":(0,0),"B":(0,4),"C":(3,0),"D":(6,4)}
I, J = coords.keys(), coords.keys()
p = 2

d = {(i,j): math.hypot(coords[i][0]-coords[j][0], coords[i][1]-coords[j][1]) for i in I for j in J}

m = pl.LpProblem("p_center", pl.LpMinimize)
x = pl.LpVariable.dicts("x", (I,J), 0, 1, pl.LpBinary)
y = pl.LpVariable.dicts("y", J, 0, 1, pl.LpBinary)
R = pl.LpVariable("R", lowBound=0)

m += R

for i in I:
    m += pl.lpSum(x[i][j] for j in J) == 1
for i in I:
    for j in J:
        m += x[i][j] <= y[j]
m += pl.lpSum(y[j] for j in J) == p
for i in I:
    m += pl.lpSum(d[(i,j)]*x[i][j] for j in J) <= R

m.solve(pl.PULP_CBC_CMD(msg=False))
sol = [j for j in J if pl.value(y[j])>0.5]
print("Оптимальные станции:", sol)
print("Макс. расстояние R =", round(pl.value(R),3))
