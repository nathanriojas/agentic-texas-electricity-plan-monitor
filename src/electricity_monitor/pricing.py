from .models import Plan, IntervalReading

def cycle_cost(plan: Plan, usage_kwh: float) -> float:
    total = plan.provider_base_charge + plan.tdu_fixed_charge + usage_kwh * (plan.provider_rate_per_kwh + plan.tdu_rate_per_kwh)
    if plan.credit_threshold_kwh is not None and usage_kwh >= plan.credit_threshold_kwh:
        total -= plan.credit_amount
    return total

def _hour_in_window(hour: float, start: float, end: float) -> bool:
    if start < end:
        return start <= hour < end
    return hour >= start or hour < end

def time_of_use_cost(plan: Plan, readings: list[IntervalReading]) -> float:
    if plan.free_start_hour is None or plan.free_end_hour is None:
        raise ValueError("TOU plan requires free_start_hour and free_end_hour")
    provider_energy = 0.0
    tdu_energy = 0.0
    for reading in readings:
        free = _hour_in_window(reading.hour, plan.free_start_hour, plan.free_end_hour)
        if not free:
            provider_energy += reading.kwh * plan.provider_rate_per_kwh
        tdu_energy += reading.kwh * plan.tdu_rate_per_kwh
    return plan.provider_base_charge + plan.tdu_fixed_charge + provider_energy + tdu_energy

def efl_tou_sample_cost(plan: Plan, usage_kwh: float, assumed_free_share: float) -> float:
    if not 0 <= assumed_free_share <= 1:
        raise ValueError("assumed_free_share must be between 0 and 1")
    provider_billable = usage_kwh * (1 - assumed_free_share)
    return plan.provider_base_charge + plan.tdu_fixed_charge + provider_billable * plan.provider_rate_per_kwh + usage_kwh * plan.tdu_rate_per_kwh
