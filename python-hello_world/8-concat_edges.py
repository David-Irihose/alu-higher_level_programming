#!/usr/bin/python3

my_str = (
    "Python is an interpreted, interactive, object-oriented programming language "
    "that combines remarkable power with very clear syntax"
)
my_str = my_str[39:66] + my_str[106:112] + my_str[:6]
print(my_str)
