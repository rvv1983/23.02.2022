# По заданному номеру дня недели вывести его название
day = int(input("enter week number "))
if day==1:
    print(f"{day} is monday")
elif day==2:
 print(f"{day} is tuesday")
elif day==3:
 print(f"{day} is wednesday")
elif day==4:
 print(f"{day} is thursday")
elif day==5:
 print(f"{day} is friday")
elif day==6:
 print(f"{day} is saterday")
elif day==7:
 print(f"{day} is sunday")
else: print("enter numbers less than 8")