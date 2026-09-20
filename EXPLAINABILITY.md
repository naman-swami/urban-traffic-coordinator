# Explainability — urban-traffic-coordinator

## Decision Reasoning
UrbanFlow models traffic as continuous compressible fluid flow, calculating shockwave propagation and Webster optimal split times to maximize corridor throughput.

## Data Sources and Inputs Used
NTCIP-compliant traffic signal controllers, inductive road loop detectors, transit CAD/AVL feeds, and municipal emergency CAD GPS dispatch.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, urban-traffic-coordinator assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, urban-traffic-coordinator will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, urban-traffic-coordinator explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
urban-traffic-coordinator actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Physical Infrastructure: Cannot repair physical traffic light hardware malfunctions or severed fiber-optic cables.
- Driver Compliance: Cannot physically force individual human drivers to obey traffic signals or clear emergency lanes.
- Weather Road Closures: Cannot reopen roads physically blocked by fallen power lines or snow drifts.
- Emergency Dispatch Authority: Does not dispatch first responders; operates traffic signals to assist designated units.

## Uncertainty Quantification Approach
When inductive loop sensors fail or report zero occupancy during known peak hours, UrbanFlow falls back to historical time-of-day timing plans and flags sensors for field maintenance.
