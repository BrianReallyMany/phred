#!/usr/env/bin python

import unittest
from phred import PhredHelper

class TestPhredHelper(unittest.TestCase):
    def test_initialize(self):
        helper1 = PhredHelper()
        self.assertEqual(33, helper1.offset)
        helper2 = PhredHelper(64)
        self.assertEqual(64, helper2.offset)

    def test_char_to_int(self):
        helper1 = PhredHelper()
        self.assertEqual(0, helper1.char_to_int('!'))






#####################################\
if __name__ == '__main__':
    unittest.main()
