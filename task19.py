# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
x = int(input('enter x  '))
y = int(input('enter y  '))
if x>0 and y>0 and x!=0 and y!=0:
    print ("это 1 четверть ")
elif x<0 and y>0 and x!=0 and y!=0:
    print ("это 2 четверть ")
elif x<0 and y<0 and x!=0 and y!=0:
    print ("это 3 четверть ")
elif x>0 and y<0 and x!=0 and y!=0:
    print ("это 4 четверть ")
else:
    print("задан ноль, выбери иной вариант значения переменной")