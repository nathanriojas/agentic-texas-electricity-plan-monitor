from dataclasses import dataclass, field
from typing import Literal

PlanType = Literal["fixed", "bill_credit", "time_of_use", "variable", "prepaid"]

@dataclass(frozen=True)
class UsageCycle:
    label: str
    kwh: float

@dataclass(frozen=True)
class IntervalReading:
    hour: float
    kwh: float

@dataclass
class Plan:
    plan_id: str
    provider: str
    name: str
    plan_type: PlanType
    term_months: int
    provider_rate_per_kwh: float
    provider_base_charge: float = 0.0
    tdu_rate_per_kwh: float = 0.0
    tdu_fixed_charge: float = 0.0
    credit_threshold_kwh: float | None = None
    credit_amount: float = 0.0
    free_start_hour: float | None = None
    free_end_hour: float | None = None
    variable: bool = False
    metadata: dict = field(default_factory=dict)
