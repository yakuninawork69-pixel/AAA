
#Создать программу, которая использует библиотеку math для вычисления квадратного корня

import math
print(math.sqrt(16))

import math
num=float(input("введите число:"))
if num>=0:
  result=math.sqrt(num)
  print("результат:", result)
else:
  print("невозможно вычислить корень из введенного числа")

