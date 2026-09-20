"""
Urban Traffic Coordinator Engine
Calculates Webster's optimal intersection cycle lengths and schedules emergency vehicle preemption waves.
"""
from typing import Dict, Any

class UrbanTrafficFlowEngine:
    def calculate_webster_cycle(self, lost_time_seconds: float, critical_flow_ratio_sum: float) -> Dict[str, Any]:
        # Webster formula: C0 = (1.5 * L + 5) / (1 - Y)
        if critical_flow_ratio_sum >= 0.95:
            # Saturation condition
            return {"cycle_length_seconds": 120.0, "status": "OVERSATURATED_DEMAND", "green_split_pct": 50.0}
        
        c0 = (1.5 * lost_time_seconds + 5) / (1.0 - critical_flow_ratio_sum)
        c0 = round(max(45.0, min(150.0, c0)), 1)

        return {
            "optimal_cycle_length_seconds": c0,
            "lost_time_seconds": lost_time_seconds,
            "critical_flow_ratio": critical_flow_ratio_sum,
            "level_of_service": "LOS_B" if c0 < 70 else "LOS_C" if c0 < 100 else "LOS_D"
        }
