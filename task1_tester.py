# Напишите программу, которая принимает на вход вещественное число, и показывает сумму его цифр
import math
n = float(input('Введите число '))
sum = 0
if n < 0:
    n = n * -1
while n - int(n) != 0:
    n = round(n * 10, 8)
n = int(n)
while n != 0:
    sum += n % 10
    n = n//10
print(n, sum)
