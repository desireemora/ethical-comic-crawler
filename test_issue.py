# test_issue.py

import unittest

from issue import Issue

class TestIssue(unittest.TestCase):
    
    def setUp(self):
        """Set up sample issue for use in all unit tests."""
        self.issue = Issue('X-men','13A','Sep 2013','Marvel')
        self.issue_generic = Issue('X-men','12','Sep 2013','Marvel')
        self.isse_variant = Issue('X-Men','13D','Sep 2013','Marvel')

    def test_isVariant(self):
        """Testing that non variants return False."""
        self.assertEqual(self.issue.isVariant(), False)
        self.assertEqual(self.issue_generic.isVariant(), False)

        """Testing that variants return True."""
        self.assertEqual(self.isse_variant.isVariant(), True)
    