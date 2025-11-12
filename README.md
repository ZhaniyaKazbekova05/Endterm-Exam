🏥 Distribution of Medical Resources Using Vogel’s Approximation Method (VAM)
📘 Project Overview

This project demonstrates how to optimize the distribution of medical resources from supply centers to hospitals using Linear Programming concepts.
The Vogel’s Approximation Method (VAM) is applied to find an initial feasible solution for the Transportation Problem, followed by an optimality check using the MODI method.

The goal is to minimize the total transportation cost while fully meeting the demand of hospitals and not exceeding available supplies.

🎯 Objectives

Apply linear programming to a real-world logistics scenario.

Implement the Vogel’s Approximation Method in Python.

Verify optimality using a simplified MODI (Modified Distribution) check.

Visualize and analyze the allocation plan and total cost.

🧩 Problem Description

Three medical supply centers distribute resources to four hospitals.
Each route has a transportation cost per unit.
We must decide how many units to send from each supply center to each hospital to minimize total cost.

Supply Centers / Hospitals	H1	H2	H3	H4
S1 (Astana)	4	6	8	13
S2 (Almaty)	5	11	9	7
S3 (Shymkent)	9	8	6	5

Supply: [120, 80, 100]
Demand: [60, 40, 90, 110]

⚙️ Methodology

Vogel’s Approximation Method (VAM)

Calculates penalties based on the difference between two smallest costs in each row and column.

Chooses the row/column with the highest penalty.

Allocates to the cell with the minimum cost within that row/column.

Repeats until all supplies and demands are satisfied.

Optimality Check (MODI)

Calculates potentials u and v for occupied cells.

Computes reduced costs Δ = c - (u + v).

If all Δ ≥ 0 → the solution is optimal.

💻 Implementation

The project is implemented in Python (NumPy).

🧠 Main Script
vogel_method.py

🚀 Run the program
python3 vogel_method.py

✅ Expected Output
Allocation plan:
[[60 40 20  0]
 [ 0  0  0 80]
 [ 0  0 70 30]]
Total cost: 1770.0
Is optimal?: True

🧾 Results Summary

Total transportation cost: 1770

All hospital demands are fully satisfied.

Optimal routes:

S1 → H1, H2

S2 → H4

S3 → H3, H4

This result confirms that Vogel’s method provides an optimal or near-optimal distribution with minimal total cost.

🧠 Concepts Covered

Linear Programming

Transportation Problem

Vogel’s Approximation Method (VAM)

MODI Optimality Check

Python implementation using NumPy

🧩 Future Improvements

Add graphical visualization of routes and cost heatmaps.

Integrate real data (distances, demand, supply) from healthcare logistics.

Include time and risk constraints for multi-objective optimization.

Compare with Simplex or Scipy linprog solver results.

👩‍💻 Author

Kazbekova Zhaniya
Astana IT University