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
tala = 0
while (len(stokkur) != 0) or (len(stokkur2) != 0):
    if tala % 2 == 0:
        print('spilið þitt er:')
        print('Nafn:', stokkur[0][0])
        print('1. Þyngd:', stokkur[0][1])
        print('2. Þyngd:', stokkur[0][2])
        print('3. Þyngd:', stokkur[0][3])
        print('4. Þyngd:', stokkur[0][4])
        print('5. Þyngd:', stokkur[0][5])
        print('6. Þyngd:', stokkur[0][6])
        print('7. Þyngd:', stokkur[0][7])
        print('8. Þyngd:', stokkur[0][8])
        val = int(input("Hvað ætlar þú að nota: "))
        if stokkur[0][val] > stokkur2[0][val]:
            print("Tölvan var með:",stokkur2[0][val])
            stokkur.append(stokkur2[0])
            stokkur2.remove(stokkur2[0])
            temp.append(stokkur[0])
            stokkur.remove(stokkur[0])
            stokkur.append(temp[0])
            temp.remove(temp[0])
            print("Sigur")
            print()
            tala += 1
        elif stokkur[0][val] < stokkur2[0][val]:
            print("Tölvan var með:", stokkur2[0][val])
            stokkur2.append(stokkur[0])
            stokkur.remove(stokkur[0])
            temp.append(stokkur2[0])
            stokkur2.remove(stokkur2[0])
            stokkur2.append(temp[0])
            temp.remove(temp[0])
            print("Tap")
            print()
            tala += 1
        else:
            print("ERROR")
    elif tala % 2 == 1:
        print('spil tölvunar er:')
        print('Nafn:', stokkur2[0][0])
        print('1. Þyngd:', stokkur2[0][1])
        print('2. Þyngd:', stokkur2[0][2])
        print('3. Þyngd:', stokkur2[0][3])
        print('4. Þyngd:', stokkur2[0][4])
        print('5. Þyngd:', stokkur2[0][5])
        print('6. Þyngd:', stokkur2[0][6])
        print('7. Þyngd:', stokkur2[0][7])
        print('8. Þyngd:', stokkur2[0][8])
        val = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        if stokkur[0][val] > stokkur2[0][val]:
            print("Þú varst með:", stokkur[0][val])
            stokkur.append(stokkur2[0])
            stokkur2.remove(stokkur2[0])
            temp.append(stokkur[0])
            stokkur.remove(stokkur[0])
            stokkur.append(temp[0])
            temp.remove(temp[0])
            print("Sigur")
            print()
            tala += 1
        elif stokkur[0][val] < stokkur2[0][val]:
            print("Þú varst með:", stokkur[0][val])
            stokkur2.append(stokkur[0])
            stokkur.remove(stokkur[0])
            temp.append(stokkur2[0])
            stokkur2.remove(stokkur2[0])
            stokkur2.append(temp[0])
            temp.remove(temp[0])
            print("Tap")
            print()
            tala += 1
        else:
            print("ERROR")




































'''
jafntefli
jafnt = []
jafnt.append(stokkur)
jafnt.append(stokkur2)
jafnt = []
'''