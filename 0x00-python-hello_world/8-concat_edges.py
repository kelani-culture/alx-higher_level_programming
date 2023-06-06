#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + " " + str[str.index("with"):].split()[0] + " " + str[0:6]
print(str)
