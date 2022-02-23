# Написать программу вычисления значения функции y = f(a)
from ast import arg

print("start game - guess the number ")
def   f(a):
    if a == 1:
        print ('bingo')
    else:
        print ('not bingo')
arg = int(input('enter number '))
print(f(arg))