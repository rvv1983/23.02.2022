# Написать программу вычисления произведения чисел от 1 до N
N = int(input("enter N: "))
proizv = 1
while (N != 0):
    proizv = proizv * (N % 10)
    N = N // 10
print("result is : ", proizv)  