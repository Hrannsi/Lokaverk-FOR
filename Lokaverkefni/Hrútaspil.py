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
temp = []

print("Þegar þú ert að velja á eftir þá notar þú tölu stafi ekki orð, þar sem 1 = þyngd, 2 = Mjólk, 3 = ull, 4 = afkvæmi, 5 = lærvöðvi, 6 = frjósemi, 7 = kjöt og 8 = rassvöðvi")

while (len(stokkur) != 0) or (len(stokkur2) != 0):
    print('spilið þitt er:')
    print('Nafn:', stokkur[0][0])
    print('1. Þyngd:', stokkur[0][1])
    val = input("Hvað ætlar þú að nota: ")
    if val == "1":
        if stokkur[0][1] > stokkur2[0][1]:
            stokkur.append(stokkur2[0])
            stokkur2.remove(stokkur2[0])
            temp.append(stokkur[0])
            stokkur.remove(stokkur[0])
            stokkur.append(temp[0])
            temp.remove(temp[0])
        elif stokkur[0][1] < stokkur2[0][1]:
            stokkur2.append(stokkur[0])
            stokkur.remove([0])
            temp.append(stokkur2[0])
            stokkur2.remove([0])
            stokkur2.append(temp[0])
            temp.remove([0])
        else:
            print("ERROR")
    else:
        print("ERROR")
    print(stokkur)
    print(stokkur2)




































'''
jafntefli
jafnt = []
jafnt.append(stokkur)
jafnt.append(stokkur2)
jafnt = []
'''