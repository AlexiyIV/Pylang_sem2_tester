#Напишите программу, которая принимает на вход два числа.
#Получите значение N, для пустого списка, заполните числами в диапазоне [-N, N].
#Найдите произведение на указазных позициях
n =int(input('введите N '))
fpos = int(input('введите позицию первого элемента '))
spos = int(input('введите позицию второго элемента '))
array = []
for i in range(-n, n+1):
        array.append(i)
if 0 < fpos <= len(array) and 0 < spos <= len(array):
    m = array[fpos-1] * array[spos-1]
    print(array)
    print(m)
else:
    print('Нет таких элементов с такими индексами')