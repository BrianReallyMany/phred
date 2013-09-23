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
        # Sanger
        helper1 = PhredHelper()
        self.assertEqual(0, helper1.char_to_int('!'))
        self.assertEqual(10, helper1.char_to_int('+'))
        self.assertEqual(27, helper1.char_to_int('<'))
        # Illumina
        helper2 = PhredHelper(64)
        self.assertEqual(0, helper2.char_to_int('@'))
        self.assertEqual(10, helper2.char_to_int('J'))
        self.assertEqual(27, helper2.char_to_int('['))

    def test_int_to_char(self):
        #Sanger
        helper1 = PhredHelper()
        self.assertEqual('I', helper1.int_to_char(40))
        self.assertEqual('?', helper1.int_to_char(30))
        self.assertEqual('5', helper1.int_to_char(20))
        # Illumina
        helper2 = PhredHelper(64)
        self.assertEqual('h', helper2.int_to_char(40))
        self.assertEqual('^', helper2.int_to_char(30))
        self.assertEqual('T', helper2.int_to_char(20))
        




#####################################\
if __name__ == '__main__':
    unittest.main()
