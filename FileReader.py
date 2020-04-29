import math
import re

f = open('MathQuestions.txt', 'r')

file_contents = f.read()

string1 = "498results should get"
map(int, re.findall(r'\d+', string1))
[498]

filepath = 'MathQuestions.txt'
with open(filepath) as fp:
   for cnt, line in enumerate(fp):
        print("Line {}: {}".format(cnt, line))

f.close()

