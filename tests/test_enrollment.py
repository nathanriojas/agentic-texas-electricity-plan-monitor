import unittest
from electricity_monitor.enrollment import FailClosedVerifier, require_verified
class EnrollmentTests(unittest.TestCase):
    def test_public_default_fails_closed(self): self.assertEqual(require_verified(["1","2"],FailClosedVerifier()),[])
if __name__=='__main__': unittest.main()
