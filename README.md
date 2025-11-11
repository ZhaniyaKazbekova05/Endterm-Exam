# 🚑 Optimal Placement of Ambulance Stations (P-Center Problem)

## 🎯 Project Goal
This project aims to determine the **optimal locations for ambulance stations** in a city to **minimize the maximum (worst-case) response distance** between any demand zone and its nearest open station.

This is formulated as a **P-Center optimization problem**, a classical linear programming model widely applied in emergency service planning, logistics, and facility location.

---

## 🧩 Model Formulation

**Decision Variables**
- `y_j = 1` if an ambulance station is opened at location *j*  
- `x_ij = 1` if demand zone *i* is served by station *j*  
- `R` = maximum service distance (to minimize)

**Objective Function**
\[
\min R
\]

**Constraints**
1. Every demand zone is assigned to one station  
   \(\sum_{j \in J} x_{ij} = 1\)
2. Assignment only if a station is open  
   \(x_{ij} \le y_j\)
3. Exactly *p* stations are opened  
   \(\sum_{j \in J} y_j = p\)
4. Distance limitation  
   \(\sum_{j \in J} d_{ij}x_{ij} \le R\)
5. \(x_{ij}, y_j \in \{0,1\}, R \ge 0\)

---

## 💻 Implementation

Two complementary approaches were implemented:

### 1. **Brute-Force Algorithm (Custom Implementation)**
- Enumerates all possible combinations of *p* stations.
- Assigns each demand zone to the nearest open station.
- Calculates and compares the maximum response distances.
- Useful for validation on small datasets.

### 2. **MILP Model using PuLP**
- Exact linear formulation solved via the built-in CBC solver.
- Confirms correctness of the mathematical model and logic.

---

## 📊 Results

| Method | Optimal Stations | Max Distance R (km) |
|---------|-----------------|--------------------:|
| Manual Enumeration | {B, D} | 5.00 |
| Brute Force (Python) | {B, D} | 5.00 |
| PuLP (MILP Solver) | {B, D} | 5.00 |

✅ All methods produced identical results — confirming the correctness of the model and code.

---

## ⚙️ How to Run (Local Setup)

1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
Install dependencies:

pip install pulp


Run the optimization script:

python src/milp_p_center_pulp.py


View the results in the terminal:

Optimal stations: ['B', 'D']
Maximum distance R = 5.0

📈 Sensitivity Analysis
Number of Stations (p)	Maximum Distance R (km)	Change (%)
1	7.21	—
2	5.00	↓ 30.7 %

➡ Increasing the number of stations significantly reduces the worst-case response distance.

🧠 Insights

The P-Center model helps minimize the maximum emergency response time.

Even adding one additional station greatly improves overall city coverage.

Verified using three independent methods — all give identical results.

The approach can be applied to medical, fire, or logistics networks.

📚 References

Daskin, M. S. (2013). Network and Discrete Location: Models, Algorithms, and Applications. John Wiley & Sons.

ReVelle, C. S., & Swain, R. W. (1970). Central facilities location problem. Geographical Analysis, 2(1), 30–42.

👩‍💻 Author

Kazbekova Zhaniya
Astana IT University — Linear Programming Endterm Project
Academic Supervisor: Karashbaeve Zhanat
Year: 2025