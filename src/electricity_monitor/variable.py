from dataclasses import dataclass

@dataclass(frozen=True)
class StressResult:
    current_savings: float
    stressed_savings: float
    survives: bool

def stress_variable_candidate(incumbent_cost: float, candidate_cost_at_current_rate: float, incumbent_cancellation_cost: float, multiplier: float = 1.10, threshold: float = 300.0) -> StressResult:
    current = incumbent_cost - candidate_cost_at_current_rate - incumbent_cancellation_cost
    stressed_candidate = candidate_cost_at_current_rate * multiplier
    stressed = incumbent_cost - stressed_candidate - incumbent_cancellation_cost
    return StressResult(current, stressed, stressed >= threshold)
