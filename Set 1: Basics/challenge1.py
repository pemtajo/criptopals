#!/usr/bin/python
# coding=UTF-8
import base64

def convert_hex_to_base64(hex):
    result = bytearray.fromhex(hex)
    return base64.b64encode(result)