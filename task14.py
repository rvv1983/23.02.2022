# Найти третью цифру числа или сообщить, что её нет
a = int(input("введите трехзначное число "))
if a<100:
    print ("третьей цифры нет ")
else:
    while a>1000:
        a=a//10
    print (a%10)