import os
import pytest
from models.webster_signal_timing import WebsterSignalOptimizer

def test_webster_cycle_calculation():
    phases = [
        {"phase_name": "NS", "critical_flow_vph": 800.0, "saturation_flow_vph": 1800.0},
        {"phase_name": "EW", "critical_flow_vph": 400.0, "saturation_flow_vph": 1800.0}
    ]
    res = WebsterSignalOptimizer.calculate_cycle_and_splits(phases, total_lost_time_l=10.0)
    assert res["optimal_cycle_seconds"] >= 45.0
    assert "NS" in res["green_phase_splits_seconds"]
    assert "EW" in res["green_phase_splits_seconds"]
    assert res["green_phase_splits_seconds"]["NS"] > res["green_phase_splits_seconds"]["EW"]

def test_oversaturated_gridlock():
    phases = [
        {"phase_name": "NS", "critical_flow_vph": 1800.0, "saturation_flow_vph": 1800.0},
        {"phase_name": "EW", "critical_flow_vph": 1800.0, "saturation_flow_vph": 1800.0}
    ]
    res = WebsterSignalOptimizer.calculate_cycle_and_splits(phases, total_lost_time_l=10.0)
    assert res["error"] == "OVERSATURATED_INTERSECTION"
