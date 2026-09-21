# Urban Traffic Coordinator & Signal Timing Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![ITS](https://img.shields.io/badge/Domain-Intelligent_Transportation_Systems-orange.svg)](docs/hcm_level_of_service.md)
[![Standard](https://img.shields.io/badge/Standard-HCM_Webster_Model-blue.svg)](docs/hcm_level_of_service.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An intelligent transportation systems (ITS) traffic signal coordination engine implementing Webster's minimum delay formulation and Highway Capacity Manual (HCM) Level of Service (LOS) grading.

```
                    ┌─────────────────────────┐
                    │  Intersection Volumes   │
                    │   (Arrival & Saturation)│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ models/webster_signal   │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Webster Formula    │         │  HCM LOS Tiers      │
      │ C_0 = (1.5L+5)/(1-Y)│         │   (LOS A through F) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Phase Green Allocation  │
                    │ (North-South / East-West│
                    └─────────────────────────┘
```

## Features

- **Webster Optimal Cycle Computation**: Minimizes total arterial vehicle delay using flow ratio sums.
- **Dynamic Green Phase Splits**: Proportional green allocation based on lane saturation indices.
- **Sensor Feeds Grounding**: Pre-configured with downtown arterial multi-phase volume telemetry.

## Directory Structure

```
urban-traffic-coordinator/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint ITS traffic provenance
├── models/
│   └── webster_signal_timing.py     # Webster cycle and green split optimizer
├── fixtures/
│   └── sensor_feeds/
│       └── downtown_arterial.json   # Benchmark loop detector volumes
├── docs/
│   └── hcm_level_of_service.md      # Highway Capacity Manual standards
├── tests/
│   └── test_agent.py                # Traffic engineering test suite
├── coordinate.py                          # Traffic optimization CLI
└── requirements.txt
```

## Quick Start

```bash
# Run signal optimization tests
pytest tests/ -v

# Optimize downtown arterial intersection
python coordinate.py --demo
```
