# Возведите число А в натуральную степень B используя цикл
a = int(input("enter number a "))
b = int(input("enter number b "))
c = a
i=1
for i in range(b - 1): a*= c
print(a)
# while i<b : 
#     c=c*a
#     i=i+1
# print (c)