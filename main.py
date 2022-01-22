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
    for i in filearray:
        n = ord(i)
        if n != ord("#"):
            r_dict.append(n)
        else:
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

default_r_cnts = [1,1,1,1]

enigma = classes.Enigma(r_dicts,default_r_cnts,plagboard,reflector)
enigma.crypt()