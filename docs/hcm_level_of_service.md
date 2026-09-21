# Highway Capacity Manual (HCM) & Webster Signal Formulation

## Webster Minimum Delay Cycle Length Formula
The optimal cycle length $C_0$ minimizing vehicle delay at an isolated signalized intersection:

$$C_0 = \frac{1.5 L + 5}{1 - Y}$$

Where:
- $L$: Total lost time per cycle in seconds (typically $L = \sum (t_{\text{yellow}} + t_{\text{all-red}} - t_{\text{startup}})$)
- $Y$: Sum of critical lane group flow ratios $Y = \sum_{i} y_i = \sum_{i} \frac{q_i}{s_i}$
- $q_i$: Arrival flow rate in vehicles per hour
- $s_i$: Saturation flow rate (typically 1,800 to 1,900 vphgpl)
