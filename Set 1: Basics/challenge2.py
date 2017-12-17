#!/usr/bin/python
# coding=UTF-8

hex2bin_map = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",    
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "A":"1010",
   "B":"1011",
   "C":"1100",
   "D":"1101",
   "E":"1110",
   "F":"1111",
   "a":"1010",
   "b":"1011",
   "c":"1100",
   "d":"1101",
   "e":"1110",
   "f":"1111",

}

def fixed_xor(hex1, hex2):
    if(len(str(hex1))!=len(str(hex2))):
        return
    return xor (to_bin(hex1), to_bin(hex2))

def xor(bin1, bin2):
    aux=''
    str1=str(bin1)
    str2=str(bin2)
    for x in range(0, len(str1)):
        if((str1[x])==(str2[x])):
            aux+=str(0)
        else:
            aux+=str(1)
    return hex(int(aux, 2))

def to_bin(hex):
    return "".join(hex2bin_map[i] for i in hex)


print (fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))