# Даны два числа. Показать большее и меньшее число
a = int(input("enter first number "))
b = int(input("enter second number "))
if a > b:
    print ("number {} is max".format (a))
    print ("number {} is min".format (b))
else: 
    print ("number {} is max".format (b))
    print ("number {} is min".format (a))
