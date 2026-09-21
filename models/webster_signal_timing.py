"""
Webster Optimal Signal Timing & Level of Service (LOS) Engine
Calculates minimum delay cycle length C_0 and effective green split allocations conforming to HCM standards.
"""
from typing import Dict, Any, List

class WebsterSignalOptimizer:
    @staticmethod
    def calculate_cycle_and_splits(
        phases: List[Dict[str, Any]],
        total_lost_time_l: float
    ) -> Dict[str, Any]:
        # Calculate flow ratios y_i = q_i / s_i
        y_values = []
        for p in phases:
            y = p["critical_flow_vph"] / max(1.0, p["saturation_flow_vph"])
            y_values.append(y)

        sum_y = sum(y_values)
        if sum_y >= 1.0:
            return {
                "error": "OVERSATURATED_INTERSECTION",
                "sum_flow_ratios": round(sum_y, 3),
                "recommendation": "ACTIVATE_CONGESTION_GRIDLOCK_MITIGATION"
            }

        # Webster Formula: C_0 = (1.5 * L + 5) / (1 - Y)
        c_opt = round((1.5 * total_lost_time_l + 5.0) / (1.0 - sum_y), 1)
        # Cap cycle between 45s and 150s
        c_bounded = max(45.0, min(150.0, c_opt))

        effective_green = c_bounded - total_lost_time_l
        splits = {}
        for p, y in zip(phases, y_values):
            g_i = round(effective_green * (y / sum_y), 1)
            splits[p["phase_name"]] = g_i

        # Determine Level of Service (LOS)
        los = "LOS_B" if sum_y < 0.60 else "LOS_C" if sum_y < 0.80 else "LOS_D" if sum_y < 0.90 else "LOS_E"

        return {
            "optimal_cycle_seconds": c_bounded,
            "total_lost_time_seconds": total_lost_time_l,
            "sum_flow_ratios": round(sum_y, 3),
            "level_of_service": los,
            "green_phase_splits_seconds": splits
        }
