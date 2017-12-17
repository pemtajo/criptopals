#!/usr/bin/python
# coding=utf-8
# Desenvolvimento Aberto
# TestParticipante.py

import sys
sys.path.append("../")

from unittest import TestCase
import unittest
from convert_hex_to_base64 import convert_hex_to_base64

__author__='pmdragon'

class TestText(unittest.TestCase):
    def test_set1(self):
        text=convert_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
        self.assertEquals(text, b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
