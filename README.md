# Urban Traffic Corridor Coordinator

> **Municipal Intelligent Transportation System (ITS) & Arterial Timing Engine**  
> Implementing Webster's Minimum-Delay Cycle Calculations and Highway Capacity Manual (HCM) Standards.

---

### Signal Optimization Formulations

Webster's optimum cycle length formulation minimizes aggregate vehicle queue delay across competing intersection phases:

$$C_{opt} = \frac{1.5 L + 5}{1 - Y}$$

Where:
- $L$: Total intersection lost time per cycle (all-red + clearance yellow intervals).
- $Y = \sum_{i=1}^n y_i$: Sum of flow-to-saturation flow ratios ($y_i = q_i / s_i$) for critical phase movements.

---

### Highway Capacity Manual (HCM) Level of Service (LOS)

| Control Delay per Vehicle | HCM Level of Service | Operational Progression | Driver Expectation |
| :--- | :--- | :--- | :--- |
| $\le 10.0\text{ sec}$ | **LOS A** | Free flow, excellent progression | Minimal stop delay |
| $> 10.0 \text{ and } \le 20.0\text{ s}$ | **LOS B** | Good progression, slight delay | Noticeable stops |
| $> 20.0 \text{ and } \le 35.0\text{ s}$ | **LOS C** | Stable operations, fair progression | Significant queuing |
| $> 35.0 \text{ and } \le 55.0\text{ s}$ | **LOS D** | Approaching unstable flow | Lengthy queues |
| $> 55.0 \text{ and } \le 80.0\text{ s}$ | **LOS E** | Unstable flow, at capacity limit | Severe congestion |
| $> 80.0\text{ sec}$ | **LOS F** | Breakdown, oversaturated gridlock | Forced stop-and-go |

---

### Corridor Progression Execution

```bash
# Coordinate downtown arterial sensor feed (Loop Detector Stream)
python coordinate.py --demo

# Run Webster timing unit test suite
pytest tests/ -v
```

Detector schemas, actuation parameters, and phase split tables are defined in [HCM_STANDARDS.md](HCM_STANDARDS.md) and `fixtures/sensor_feeds/`.
