import unittest
from electricity_monitor.dedupe import recommendation_fingerprint
class DedupeTests(unittest.TestCase):
    def test_order_and_small_savings_change_do_not_matter(self):
        self.assertEqual(recommendation_fingerprint(["2","1"],351),recommendation_fingerprint(["1","2"],349))
if __name__=='__main__': unittest.main()
