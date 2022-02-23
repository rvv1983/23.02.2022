# Выяснить является ли число чётным
a = int(input("enter  number  "))
if a%2==0 and a!=0:
    print("the number is even")
elif a%2==1 and a!=0:
    print("the number is not even")
else:
    print ("zero")
