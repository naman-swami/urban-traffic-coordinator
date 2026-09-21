import argparse
import json
import os
from models.webster_signal_timing import WebsterSignalOptimizer

def main():
    parser = argparse.ArgumentParser(description="Urban Traffic Coordinator CLI")
    parser.add_argument("--demo", action="store_true", help="Optimize downtown intersection timing")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "sensor_feeds", "downtown_arterial.json")

    if args.demo:
        with open(data_file, "r") as f:
            d = json.load(f)

        res = WebsterSignalOptimizer.calculate_cycle_and_splits(
            phases=d["phases"],
            total_lost_time_l=d["lost_time_seconds"]
        )

        print("=== URBAN TRAFFIC SIGNAL OPTIMIZATION REPORT ===\n")
        print(f"Intersection: {d['intersection_id']}")
        print(f"Sum of Flow Ratios (Y): {res['sum_flow_ratios']} | Level of Service: {res['level_of_service']}")
        print(f"Optimal Cycle Length (C_0): {res['optimal_cycle_seconds']} seconds (Lost Time: {res['total_lost_time_seconds']}s)\n")
        print("Green Phase Split Allocation:")
        for phase, green in res["green_phase_splits_seconds"].items():
            print(f"  * {phase}: {green} seconds green time")
        print()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
