"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazin. Elemanlari birden çok katmanli listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

listF = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
FlattenList = listF()

def flatten(x):
    for i in x:
        if type(i) == listF:
            flatten(i)
        else:
            FlattenList.append(i)
flatten(listF)
print(FlattenList)