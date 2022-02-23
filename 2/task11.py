# 11 Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# N = int( input(" enter num  "))
# posl=[]
# a=1
# for i in range (1,N+1):
#   posl.append(a)
#   a*=-3
 
# print(posl)

# 12 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# list=[]
# n=2
# for i in range(1,n+1):
#     list.append("{} : {} ".format(i,3*i+1))
# print (list)

# 13   Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# a={1,2,3,4}
# b={3,4,5,6}
# i=a.intersection(b)
# print(i)

# 14  Подсчитать сумму цифр в вещественном числе.
# N=input("enter N")
# sum=0
# for i in range(0,len(N)):
#     if N!=".":
#        sum=sum+int(N[i])
# print(sum)




# 15  Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
# N = int(4)
# posl=[]
# a=1
# for i in range (1,N+1):
#   a=a*(i)
#   posl.append(a)
# print(posl)



# 16  задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

# list=[]
# num=1
# sum=0
# N = int(input(" enter N  "))
# for i in range (1,N+1):
#     list.append(num)
#     num=(1+1/i)**i   
#     sum+=num
# print(list)
# print(sum)

#  17  Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt   в одной строке одно число
# list=[]
# num=1
# sum=0
# N = int(input(" enter N  "))
# for i in range (1,N+1):



 # 18  Реализовать алгоритм перемешивания списка. 
# import random
# list=[1,2,5,8,9]
# for i in range(len(list)):
#     index = random.randint(0,len(list)-1)
#     list[i],list[index]=list[index],list[i]
# print(list)

# 19 Реализовать алгоритм задания случайных чисел. Без использования встроенного 
#  генератора псевдослучайных чисел
# import random
# list=[]
# num=1
# sum=0
# N = int(input(" enter N  "))
# for i in range (1,N+1):
#     list.append(num)
#     num=(1+i)   
# List=num    
# for i in range(len(list)):
#       index = random.randint(0,len(list)-1)
#       list[i],list[index]=list[index],list[i]
# print(list)


 # 20 Определить, присутствует ли в заданном списке строк, некоторое число 

# list=["1","55","rty","pop","rok","5"]
# N = int( input(" enter num  "))
# count=0
# for i in range(len(list)):
#     if str(N) in list[i]:
#         print("число находится в ", i+1, "строке списка")
#         count =1
# if count == 0:
#     print("числа нет в списке ")

# 21 Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

#  Найти сумму чисел списка стоящих на нечетной позиции
# import random
# a=3
# su=0
# q=0
# for b in range(a):
#     c=random.randint(1,11)
#     print(c," ")
# if c%2==0
    
# print(su)

# 22 Найти сумму чисел списка стоящих на нечетной позиции
# list = [1,2,3,4,5,6,7]
# sum = 0
# for i in range(0,len(list),2):
#     sum+=list[i]
# print(sum)


# 23 и т.д.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
#    второй и предпоследний  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# list=[2, 3, 4, 5, 6]
# def mult(element):
#     list2 = []
#     while len(element) > 1:
#         list2.append(element[0]*element[-1])
#         del element[0] 
#         del element[-1] 
#     if len(element) ==1: list2.append(element[0]**2)       
#     return list2
# print(mult(list))




# 24 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# float_list=[1.1,2.34,3.94,2.54,1.23]
# list=[]
# max_num=0
# min_num=0
# for i in float_list:
#     list.append(round(i%1,2))
# print(list)
# for i in list:
#     max_num=max(i)
#     min_num=min(i)

# 25  Написать программу преобразования десятичного числа в двоичное
# n=int(input())
# b=" "
# while n>0:
#     b=str(n%2)+b
#     n=n//2
# print(b)

# 26  Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 # Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# fib = int(input('please provide the size of the sequence: '))
#     a1 = 0
#     a2 = 1
#     a3 = 0
#     fib_sequence = []
#     fib_sequence.append(a1)
#     fib_sequence.append(a2)
#     for i in range(fib):
#         a3 = a1 + a2
#         fib_sequence.append(a3)
#         a1 = a2
#         a2 = a3
#     a1 = 0
#     a2 = -1
#     a3 = 0
#     for i in range(1,fib+1):
#         a3 = a1 - a2
#         fib_sequence.insert(0,a3)
#         a1 = a2
#         a2 = a3
#     print(fib_sequence)


# 27 Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
# list="1 2 3 4"
# newlist=list.split()
# print(newlist)
# a=(newlist)
# max= (max(a))
# min= (min(a))
# print ("the max number is  ",max)
# print("the min number is  ",min)

# 28  Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
# import math
# a = int(input("Введите значение a= "))
# b = int(input("Введите значение b= "))
# c = int(input("Введите значение c= "))
# D = b ** 2 - 4 * a * c
# print(D)
# if D < 0:
#   print("Корней нет")
# elif D == 0:
#   x = -b / 2 * a
#   print (x)
# else:
#   x1 = (-b + math.sqrt(D)) / (2 * a)
#   x2 = (-b - math.sqrt(D)) / (2 * a)
#   print(x1)
#   print(x2)

# 29  Найти НОК двух чисел
# a, b = 24, 54
# i = min(a, b)
# while True:
#     if i%a==0 and i%b==0:
#         break
#     i += 1
# print(i)




# 30 Вычислить число  c заданной точностью d
#	Пример: при d = 0.001, п = 3.141. 10-1d10-10 
# Initialize denominator
# k = 1
# # Initialize sum
# s = 0
# for i in range ( 1000000 ):
# # even index elements are positive
# if i % 2 = = 0 :
# s + = 4 / k
# else :
# # odd index elements are negative
# s - = 4 / k
# # denominator is odd
# k + = 2
# print (s)


# list=[i for i in range (1,21) ]
# # for i in range (1,10):
# #     if (i%2==0):
# #      list.append(i)
# print(list) 




# Из лекции 3 вырезка

# from types import LambdaType


# def select(f,col):
#     return[f(x) for x in col]
# def where(f,col):
#     return[x for x in col if f(x)]

# data="1 2 3 5 8 15 23 38".split()
# res=select(int,data)
# res=where(lambda x: not x%2, res)
# res=select(lambda x:(x,x**2),res)  
# print(res)


# 32 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#  Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]





# k = 3
# lst = [random.randint(0, 100) for i in range(k + 1)]
# print(lst)

# li = []
# for i in range(len(lst)):
#     li.append(str(lst[i]) + '*x ^ ' + str(k - i) + ' + ')

# li.pop()
# li.append(str(lst[-1]))
# li.append(' = 0')
# text = ''.join(li)
# print(text)


# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(text)
