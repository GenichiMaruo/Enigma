import random

with open("data/base.txt",'r') as f:
    basearray = [s.strip() for s in f.readlines()]

cnt = input("count :")
seed = input("seed  :")

outputlen = []
random.seed(int(seed))
for i in range(int(cnt)):
    outputlen.extend(random.sample(basearray,len(basearray)))
    outputlen.append("#")
for i in range(len(outputlen)):
    outputlen[i] += "\n"

out_file_name = "data/rotors.txt"
with open(out_file_name,'w') as out_file:
    out_file.writelines(outputlen)