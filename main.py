import sys
from sys import byteorder
import os

import classes

rotors_path = "data/rotors.txt"
reflector_path = "data/reflector.txt"
plagboard_path = "data/plagboard.txt"
r_dict = []
r_dicts = []
with open(rotors_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    d = 97
    for i in filearray:
        n = ord(i)
        if n != ord("#"):
            r_dict.append([d, n])
            d += 1
        else:
            d = 97
            r_dicts.append(r_dict)
            r_dict = []
print(r_dicts)

with open(reflector_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    swap_word = []
    reflector = []
    for i in filearray:
        swap_word.append(ord(i))
        if len(swap_word) != 1:
            reflector.append(swap_word)
            swap_word = []
print(reflector)

with open(plagboard_path,'r') as f:
    filearray = [s.strip() for s in f.readlines()]
    swap_word = []
    plagboard = []
    for i in filearray:
        swap_word.append(ord(i))
        if len(swap_word) != 1:
            plagboard.append(swap_word)
            swap_word = []
print(plagboard)

length = 1
in_list = []
files = sys.argv
file = files[1]
with open(file,'r') as f:
    while i := f.read(length):
        in_list.append(ord(i))

default_r_cnts = [1,1,1,1]

print(in_list)

enigma = classes.Enigma(r_dicts,default_r_cnts,plagboard,reflector)
out_list = enigma.crypt(in_list)

out_file_name = "out.txt"
with open(out_file_name,'w') as out_file:
    out_array = [chr(n) for n in out_list]
    out_file.writelines(out_array)