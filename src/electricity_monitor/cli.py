import argparse
from .comparison import compare_fixed_plan
from .models import Plan, UsageCycle
from .variable import stress_variable_candidate

def run_demo() -> None:
    cycles = [UsageCycle("cycle-1",1450),UsageCycle("cycle-2",1320),UsageCycle("cycle-3",1180),UsageCycle("cycle-4",980),UsageCycle("cycle-5",860),UsageCycle("cycle-6",790)]
    incumbent = Plan("incumbent","Example Incumbent","Incumbent 14","bill_credit",14,0.105,5.0,0.060,4.0,1000,30.0)
    fixed = Plan("fixed-12","Example Energy","Example Fixed 12","fixed",12,0.045,0.0,0.060,4.0)
    fixed_result = compare_fixed_plan(incumbent,fixed,cycles,140.0,300.0)
    variable_current_cost = fixed_result.incumbent_cost - 465.0
    variable = stress_variable_candidate(fixed_result.incumbent_cost,variable_current_cost,140.0,1.10,300.0)
    print("\nTEXAS ELECTRICITY MONITOR — DEMO")
    print("="*56)
    print(f"Incumbent projected cost: ${fixed_result.incumbent_cost:,.2f}")
    print("Current cancellation cost: $140.00\n")
    print("1. Example Fixed 12")
    print(f"   candidate cost: ${fixed_result.candidate_cost:,.2f}")
    print(f"   projected net savings: ${fixed_result.net_savings:,.2f}")
    print("   decision: " + ("ACTIONABLE" if fixed_result.actionable else "MONITOR ONLY"))
    print("\n2. Example Variable Flex")
    print(f"   current-rate savings: ${variable.current_savings:,.2f}")
    print(f"   +10% stress savings: ${variable.stressed_savings:,.2f}")
    print("   decision: " + ("ESCALATE" if variable.survives else "MONITOR ONLY"))

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("command",choices=["demo"]); args=parser.parse_args();
    if args.command=="demo": run_demo()

if __name__ == "__main__": main()
