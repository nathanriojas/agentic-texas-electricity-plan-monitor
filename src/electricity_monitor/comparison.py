from dataclasses import dataclass
from .models import Plan, UsageCycle
from .pricing import cycle_cost

@dataclass(frozen=True)
class ComparisonResult:
    candidate_cost: float
    incumbent_cost: float
    incumbent_cancellation_cost: float
    net_savings: float
    actionable: bool

def compare_fixed_plan(incumbent: Plan, candidate: Plan, cycles: list[UsageCycle], incumbent_cancellation_cost: float, min_net_savings: float = 300.0) -> ComparisonResult:
    incumbent_cost = sum(cycle_cost(incumbent, c.kwh) for c in cycles)
    candidate_cost = sum(cycle_cost(candidate, c.kwh) for c in cycles)
    net = incumbent_cost - candidate_cost - incumbent_cancellation_cost
    return ComparisonResult(candidate_cost, incumbent_cost, incumbent_cancellation_cost, net, net >= min_net_savings)
