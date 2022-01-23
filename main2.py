import sys
from sys import byteorder
import os

import classes

rotors_path = "data/rotors.txt"
reflector_path = "data/reflector.txt"
plagboard_path = "data/plagboard.txt"
r_dict = []
r_dicts = []
with open("data/base.txt",'r') as f:
    basearray = [s.strip() for s in f.readlines()]

with open(rotors_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    d = 0
    for i in filearray:
        n = ord(i)
        if n != ord("#"):
            r_dict.append([ord(basearray[d]), n])
            d += 1
        else:
            d = 0
            r_dicts.append(r_dict)
            r_dict = []

with open(reflector_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    swap_word = []
    reflector = []
    for i in filearray:
        swap_word.append(ord(i))
        if len(swap_word) != 1:
            reflector.append(swap_word)
            swap_word = []

with open(plagboard_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    swap_word = []
    plagboard = []
    for i in filearray:
        swap_word.append(ord(i))
        if len(swap_word) != 1:
            plagboard.append(swap_word)
            swap_word = []

length = 1
in_word = input("input word  : ")
in_list = []
for i in range(len(in_word)):
    in_list.append(ord(in_word[i]))

key = int(input("ini_key :"))
default_r_cnts = []
for k in range(len(r_dicts)):
    if key != 0:
        default_r_cnts.insert(0, key % 10)
        key = int(key / 10)
    else:
        default_r_cnts.append(0)

enigma = classes.Enigma(r_dicts,default_r_cnts,plagboard,reflector)
out_list = enigma.crypt(in_list)

out_word = ""
for i in range(len(out_list)):
    out_word += chr(out_list[i])

print("output word :",out_word)