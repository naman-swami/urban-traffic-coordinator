import json
import argparse
from src.traffic_engine import UrbanTrafficFlowEngine

def main():
    parser = argparse.ArgumentParser(description="UrbanFlow Traffic Coordinator CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated Webster cycle length calculation")
    args = parser.parse_args()

    engine = UrbanTrafficFlowEngine()
    report = engine.calculate_webster_cycle(lost_time_seconds=12.0, critical_flow_ratio_sum=0.72)
    print("="*60)
    print(" URBANFLOW ARTERIAL SIGNAL TIMING REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
