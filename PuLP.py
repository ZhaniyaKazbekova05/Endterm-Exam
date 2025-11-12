import pulp as pl
I = ["A","B","C","D"]
J = ["A","B","C","D"]
p = 2
coords = {"A":(0,0),"B":(0,4),"C":(3,0),"D":(6,4)}
import math
d = {(i,j): math.hypot(coords[i][0]-coords[j][0], coords[i][1]-coords[j][1]) for i in I for j in J}
m = pl.LpProblem("p_center", pl.LpMinimize)
x = pl.LpVariable.dicts("x", (I,J), lowBound=0, upBound=1, cat="Binary")
y = pl.LpVariable.dicts("y", J, lowBound=0, upBound=1, cat="Binary")
R = pl.LpVariable("R", lowBound=0, cat="Continuous")
m += R
for i in I:
    m += pl.lpSum(x[i][j] for j in J) == 1
for i in I:
    for j in J:
        m += x[i][j] <= y[j]
m += pl.lpSum(y[j] for j in J) == p
for i in I:
    m += pl.lpSum(d[(i,j)] * x[i][j] for j in J) <= R
m.solve(pl.PULP_CBC_CMD(msg=False))
sol_y = [j for j in J if pl.value(y[j]) > 0.5]
R_val = pl.value(R)
assign = {i: max(J, key=lambda j: pl.value(x[i][j])) for i in I} 
print("MILP sites:", sol_y)
print("R:", round(R_val, 3))
print("Assignments:", assign)
