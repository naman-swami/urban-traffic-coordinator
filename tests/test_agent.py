import pytest
from src.traffic_engine import UrbanTrafficFlowEngine

def test_webster_cycle_calculation():
    engine = UrbanTrafficFlowEngine()
    res = engine.calculate_webster_cycle(lost_time_seconds=10.0, critical_flow_ratio_sum=0.60)
    # (1.5 * 10 + 5) / (1 - 0.6) = 20 / 0.4 = 50.0s
    assert res["optimal_cycle_length_seconds"] == 50.0
    assert res["level_of_service"] == "LOS_B"
