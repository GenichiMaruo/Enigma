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
in_list = []
files = sys.argv
file = files[1]
with open(file,'r') as f:
    while i := f.read(length):
        in_list.append(ord(i))

key = input("ini_key :")
default_r_cnts = []
for k in range(len(r_dicts)):
    if len(key) > k:
        default_r_cnts.append(ord(key[k])-96)
    else:
        default_r_cnts.append(0)

enigma = classes.Enigma(r_dicts,default_r_cnts,plagboard,reflector)
out_list = enigma.crypt(in_list)

out_file_name = "out.txt"
with open(out_file_name,'w') as out_file:
    out_array = [chr(n) for n in out_list]
    out_file.writelines(out_array)