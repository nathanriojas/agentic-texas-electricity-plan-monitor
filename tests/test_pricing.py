import unittest
from electricity_monitor.models import Plan, IntervalReading
from electricity_monitor.pricing import cycle_cost, time_of_use_cost, efl_tou_sample_cost

class PricingTests(unittest.TestCase):
    def test_bill_credit_threshold(self):
        p=Plan("p1","Test","Credit","bill_credit",12,0.10,5,0.06,4,1000,30)
        self.assertAlmostEqual(cycle_cost(p,999),5+4+999*0.16)
        self.assertAlmostEqual(cycle_cost(p,1000),5+4+1000*0.16-30)
    def test_tou_replay(self):
        p=Plan("tou","Test","Free Nights","time_of_use",12,0.05,10,0.06,4,free_start_hour=23,free_end_hour=6)
        r=[IntervalReading(1,1.0),IntervalReading(12,1.0)]
        self.assertAlmostEqual(time_of_use_cost(p,r),10+4+1*0.05+2*0.06)
    def test_efl_assumption(self):
        p=Plan("tou","Test","Free Nights","time_of_use",12,0.05,10,0.06,4,free_start_hour=23,free_end_hour=6)
        self.assertAlmostEqual(efl_tou_sample_cost(p,1000,0.35),10+4+650*0.05+1000*0.06)
if __name__=='__main__': unittest.main()
