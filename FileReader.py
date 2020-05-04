import math
import re

f=open("MathQuestions.txt","r")
line1 = f.readlines()[0]
f.close()

# lista = []
# for i in line1:
#     lista.append(i)
#
# int1 = int(lista[0])
# operator = lista[2]
# int2 = int(lista[4])
#
# if operator == "+":
#     result = int1 + int2
#     print(result)


x = 0

for i in line1:
    print(i)
    if i != ' ' and i != '\n' and i != '+':

        x += int(i)


print(x)



# line1 = f.readline()
# print(line1)
#
# line2 = f.readline()
# print(line2)
#
# line3 = f.readline()
# print(line3)
#
# line4 = f.readline()
# print(line4)
#
# f.close();



# filepath = 'MathQuestions.txt'
# with open(filepath) as fp:
#    for cnt, line in enumerate(fp):
#         print("Line {}: {}".format(cnt, line))