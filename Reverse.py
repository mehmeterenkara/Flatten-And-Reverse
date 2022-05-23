"""
2- Verilen listenin içindeki elemanlari tersine döndüren bir fonksiyon yazin. Eğer listenin içindeki
elemanlar da liste içeriyorsa onlarin elemanlarini da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

from re import L

from flatten import FlattenList


ListF = [[1, 2], [3, 4], [5, 6, 7]]
FlattenList = list()
def listReverse(x):
    x = x[::-1]
    for i in range(len(x)):
        if type(i) == list:
            listReverse(i)
        else:
            FlattenList.append(x[i][::-1])
listReverse(ListF)
print(FlattenList)