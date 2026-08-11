import unittest
from electricity_monitor.variable import stress_variable_candidate
class VariableTests(unittest.TestCase):
    def test_current_can_fail_stress(self):
        r=stress_variable_candidate(1400,940,140,1.10,300)
        self.assertGreater(r.current_savings,300); self.assertLess(r.stressed_savings,300); self.assertFalse(r.survives)
if __name__=='__main__': unittest.main()
