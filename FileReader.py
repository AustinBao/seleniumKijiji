import math
import re

f=open("MathQuestions.txt","r")
line1 = f.readlines()[0]
f.close()

var1 = line1[0].strip().split(" ")
var2 = line1[4].strip().split(" ")
operator = line1[2].strip().split(" ")

int1 = [int(line1[0]) for line1 in var1]
int2 = [int(line1[0]) for line1 in var2]
# operator = [int(line1[0]) for line1 in operator]


if operator == '/':
    resultDivi = int1 / int2
    print(int1 + " " + operator + " " + int2 + " = " + resultDivi)

if operator == '-':
    resultSub = int1 - int2
    print(int1 + " " + operator + " " + int2 + " = " + resultSub)

if operator == '*':
    resultMulti = int1 * int2
    print(int1 + " " + operator + " " + int2 + " = " + resultMulti)

if operator == '+':
    resultAdd = int1 + int2
    print(int1 + " " + operator + " " + int2 + " = " + resultAdd)

print(int1)
print(int2)
print(operator)
print(var1)
print(var2)
print(resultAdd)
print(resultSub)
print(resultMulti)
print(resultDivi)


f.close()



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