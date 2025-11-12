import numpy as np

# --- Input data ---
costs = np.array([
    [4, 6, 8, 13],   # S1 -> H1..H4
    [5, 11, 9, 7],   # S2
    [9, 8, 6, 5]     # S3
])
supply = [120, 80, 100]
demand = [60, 40, 90, 110]

# --- Vogel's Approximation Method ---
def vogel_method(costs, supply, demand):
    supply = supply.copy()
    demand = demand.copy()
    m, n = costs.shape
    alloc = np.zeros((m, n))

    while sum(supply) > 0 and sum(demand) > 0:
        # calculate penalties for rows and columns
        row_pen = [np.partition([costs[i, j] for j in range(n) if demand[j] > 0], 1)[:2].ptp()
                   if supply[i] > 0 else -1 for i in range(m)]
        col_pen = [np.partition([costs[i, j] for i in range(m) if supply[i] > 0], 1)[:2].ptp()
                   if demand[j] > 0 else -1 for j in range(n)]

        # find largest penalty
        if max(row_pen) >= max(col_pen):
            i = np.argmax(row_pen)
            j = np.argmin([costs[i, jj] if demand[jj] > 0 else np.inf for jj in range(n)])
        else:
            j = np.argmax(col_pen)
            i = np.argmin([costs[ii, j] if supply[ii] > 0 else np.inf for ii in range(m)])

        # allocate
        x = min(supply[i], demand[j])
        alloc[i, j] = x
        supply[i] -= x
        demand[j] -= x

    total_cost = (alloc * costs).sum()
    return alloc, total_cost

# --- Simple Optimality Check ---
def check_optimality(costs, alloc):
    m, n = costs.shape
    u, v = [None]*m, [None]*n
    u[0] = 0  # start potential
    updated = True

    # find potentials
    while updated:
        updated = False
        for i in range(m):
            for j in range(n):
                if alloc[i, j] > 0:
                    if u[i] is not None and v[j] is None:
                        v[j] = costs[i, j] - u[i]; updated = True
                    elif v[j] is not None and u[i] is None:
                        u[i] = costs[i, j] - v[j]; updated = True

    # compute reduced costs
    for i in range(m):
        for j in range(n):
            if alloc[i, j] == 0:
                delta = costs[i, j] - ((u[i] or 0) + (v[j] or 0))
                if delta < 0:
                    return False
    return True

# --- Run ---
alloc, total = vogel_method(costs, supply, demand)
is_opt = check_optimality(costs, alloc)

print("Allocation plan:\n", alloc.astype(int))
print("Total cost:", total)
print("Is optimal?:", is_opt)
