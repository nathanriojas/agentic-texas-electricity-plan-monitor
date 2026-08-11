import unittest
from electricity_monitor.comparison import compare_fixed_plan
from electricity_monitor.models import Plan, UsageCycle
class ComparisonTests(unittest.TestCase):
    def test_etf_reduces_switch_savings(self):
        i=Plan("i","Incumbent","Incumbent","fixed",12,0.18)
        c=Plan("c","Candidate","Candidate","fixed",12,0.10)
        result=compare_fixed_plan(i,c,[UsageCycle("1",1000) for _ in range(6)],140,300)
        self.assertAlmostEqual(result.net_savings,340.0); self.assertTrue(result.actionable)
if __name__=='__main__': unittest.main()
