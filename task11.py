# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
a=random.randint (10,99)
print (a)
a1=(a%10)
a2=(a//10)
print (max(a2,a1))