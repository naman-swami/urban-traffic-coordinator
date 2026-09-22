# Municipal Traffic Engineering Standards & Highway Capacity Manual

## 1. Regulatory Context & Engineering Guidelines
Urban Traffic Corridor Coordinator models signalized arterial traffic networks in accordance with:
- **Highway Capacity Manual (HCM 7th Edition: A Guide for Multimodal Mobility Analysis)**
- **FHWA Manual on Uniform Traffic Control Devices (MUTCD 11th Edition)**
- **ITE (Institute of Transportation Engineers) Traffic Engineering Handbook**

---

## 2. Webster's Minimum-Delay Signal Timing Formulation
The timing optimization engine determines optimal cycle length ($C_{opt}$) to minimize overall vehicular delay:

$$C_{opt} = \frac{1.5 L + 5}{1 - Y}$$

Where:
- $L$: Total lost time per cycle ($	ext{seconds}$), calculated as $L = \sum (t_{li} + t_{yi})$ (start-up lost time plus yellow/all-red clearance intervals).
- $Y$: Aggregate critical flow ratio, $Y = \sum_{i=1}^{\phi} y_i$, where $y_i = \frac{q_i}{s_i}$.
- $q_i$: Design hour volume for critical lane group $i$ ($	ext{vehicles/hour}$).
- $s_i$: Saturation flow rate for critical lane group $i$ ($	ext{vehicles/hour of green}$).

*Feasibility Boundary*: $Y$ must be strictly less than $0.90$. If $Y \ge 0.90$, the intersection operates in oversaturation, and delay models transition to Akçelik's queue overflow equations.

---

## 3. HCM Level of Service (LOS) Delay Criteria
Level of service for signalized intersections is defined strictly in terms of control delay per vehicle:

| Level of Service (LOS) | Control Delay per Vehicle ($d$) | Traffic Operational Characteristics |
| :--- | :--- | :--- |
| **LOS A** | $d \le 10.0\text{ sec}$ | Extremely favorable progression; most vehicles arrive during green. |
| **LOS B** | $10.0 < d \le 20.0\text{ sec}$ | Good progression; short cycle lengths; light queuing. |
| **LOS C** | $20.0 < d \le 35.0\text{ sec}$ | Stable operation; fair progression; longer cycles noticeable. |
| **LOS D** | $35.0 < d \le 55.0\text{ sec}$ | Approaching congestion; noticeable queue formation on side streets. |
| **LOS E** | $55.0 < d \le 80.0\text{ sec}$ | Operations at capacity; poor progression; long cycle delays. |
| **LOS F** | $d > 80.0\text{ sec}$ | Oversaturation; intersection breakdown; queues spill back through upstream nodes. |

---

## 4. Arterial Coordination & Green Wave Bandwidth
To maximize arterial progression along multi-intersection downtown corridors:
- Offset calculation enforces bidirectional green wave coordination using the half-integer rule: $T_{travel} = \frac{D}{V_{progression}}$.
- Minimum pedestrian walk intervals ($7.0\text{ sec}$) and clearance intervals ($d_{\text{cross}} / 3.5\text{ ft/s}$) are hard constraints that cannot be preempted by vehicular green splits.
