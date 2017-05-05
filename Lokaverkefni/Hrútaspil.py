#Hrannar Örn Eyþórsson
from random import *
listi = []
with open("Hrutar.txt") as f:
    for line in f:
        listi.append(eval(line))
stokkur = []
stokkur2 = []
aftur = []
while len(stokkur) != len(listi)/2:
    val = choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    if val not in aftur:
        stokkur.append(listi[val])
        aftur.append(val)
while len(stokkur2) != len(listi)/2:
    val2 = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    if val2 not in aftur:
        stokkur2.append(listi[val2])
        aftur.append(val2)
print(stokkur)
print()
print(stokkur2)







































'''
jafntefli
jafnt = []
jafnt.append(stokkur)
jafnt.append(stokkur2)
jafnt = []
'''