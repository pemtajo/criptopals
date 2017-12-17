#!/usr/bin/python
# coding=utf-8
# Desenvolvimento Aberto
# TestParticipante.py

import sys
sys.path.append("../")

from unittest import TestCase
import unittest
from challenge1 import convert_hex_to_base64
from challenge2 import fixed_xor

__author__='pmdragon'

class TestText(unittest.TestCase):
    def test_set1(self):
        text=convert_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
        self.assertEqual(text, b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    
    def test_set2(self):
        text=fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
        self.assertEqual(text, '0x746865206b696420646f6e277420706c6179')
    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
