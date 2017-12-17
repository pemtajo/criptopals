#!/usr/bin/python
# coding=UTF-8
import base64

def convert_hex_to_base64(hex):
    result = bytearray.fromhex(hex)
    return base64.b64encode(result)

convert_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')