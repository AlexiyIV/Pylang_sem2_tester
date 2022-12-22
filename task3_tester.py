# задайте список из N чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
n = int(input('Введите количество элементов списка '))
sum = 0
array = [(1+1/i)**i for i in range(1,n+1)]
for i in range(len(array)):
    sum += array[i]
print(array)
print(sum)