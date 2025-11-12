import numpy as np
costs = np.array([
    [4, 6, 8, 13], 
    [5, 11, 9, 7],   
    [9, 8, 6, 5]    
])
supply = [120, 80, 100]
demand = [60, 40, 90, 110]
def vogel_method(costs, supply, demand):
    supply = supply.copy()
    demand = demand.copy()
    m, n = costs.shape
    alloc = np.zeros((m, n))
    while sum(supply) > 0 and sum(demand) > 0:
        row_pen, col_pen = [], []
        for i in range(m):
            if supply[i] > 0:
                active_costs = [costs[i, j] for j in range(n) if demand[j] > 0]
                if len(active_costs) > 1:
                    s = sorted(active_costs)
                    pen = s[1] - s[0]
                elif len(active_costs) == 1:
                    pen = active_costs[0]
                else:
                    pen = -1
            else:
                pen = -1
            row_pen.append(pen)
        for j in range(n):
            if demand[j] > 0:
                active_costs = [costs[i, j] for i in range(m) if supply[i] > 0]
                if len(active_costs) > 1:
                    s = sorted(active_costs)
                    pen = s[1] - s[0]
                elif len(active_costs) == 1:
                    pen = active_costs[0]
                else:
                    pen = -1
            else:
                pen = -1
            col_pen.append(pen)
        if max(row_pen) >= max(col_pen):
            i = np.argmax(row_pen)
            j = np.argmin([costs[i, jj] if demand[jj] > 0 else np.inf for jj in range(n)])
        else:
            j = np.argmax(col_pen)
            i = np.argmin([costs[ii, j] if supply[ii] > 0 else np.inf for ii in range(m)])
        x = min(supply[i], demand[j])
        alloc[i, j] = x
        supply[i] -= x
        demand[j] -= x
    total_cost = (alloc * costs).sum()
    return alloc, total_cost
def check_optimality(costs, alloc):
    m, n = costs.shape
    u, v = [None]*m, [None]*n
    u[0] = 0
    updated = True
    while updated:
        updated = False
        for i in range(m):
            for j in range(n):
                if alloc[i, j] > 0:
                    if u[i] is not None and v[j] is None:
                        v[j] = costs[i, j] - u[i]; updated = True
                    elif v[j] is not None and u[i] is None:
                        u[i] = costs[i, j] - v[j]; updated = True

    for i in range(m):
        for j in range(n):
            if alloc[i, j] == 0:
                delta = costs[i, j] - ((u[i] or 0) + (v[j] or 0))
                if delta < 0:
                    return False
    return True
alloc, total = vogel_method(costs, supply, demand)
is_opt = check_optimality(costs, alloc)
print("Allocation plan:\n", alloc.astype(int))
print("Total cost:", total)
print("Is optimal?:", is_opt)
