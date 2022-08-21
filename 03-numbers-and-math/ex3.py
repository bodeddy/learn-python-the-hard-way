"""
Math symbols for python:
+ plus (addition)
- minus (subtraction)
/ slash (divide)
* asterisk (multiply)
% percent (Modulo Operator)
< less-than
> greater-than
<= less-than-equal
>= greater-than-equal
"""

# prints the string specified in the parenthesis
print("I will now count my chickens:")

# Prints the string "hens" and the calculation of the sum, which is a floating point integer
print("Hens", 25.0 + 30.0 / 6.0)

#Prints the string "Roosters" and the calculation of the sum, which is a floating point integer
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

# Prints the string specified in the parenthesis
print("Now I will count the eggs:")

# Prints the calculation of the sum, which will be a floating point integer
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

# Prints the string specified in the parenthesis
print("Is it true that 3 + 2 < 5 - 7?")

# After calculating the sum, either True or False will be given. In this case it is False, as the answer to 3 + 2 is not less than the answer to 5 - 7
print(3 + 2 < 5 - 7)

# Prints the string followed by the answer to the sum given, which will be an integer
print("What is 3 + 2?", 3.0 + 2.0)

# Prints the string followed by the answer to the sum given, which will be an integer
print("What is 5 - 7?", 5.0 - 7.0)

# Prints the string specified in the parenthesis
print("Oh that's why it's False.")

# Prints the string specified in the parenthesis
print("How about some more.")

# Prints the string followed by True, as 5 is greater than -2
print("Is it greater?", 5 > -2)

# Prints the string followed by True, as 5 is greater or equal to -2
print("Is it greater or equal?", 5 >= -2)

# Prints the string followed by False, as 5 is not less than or equal to -2
print("Is it less or equal?", 5 <= -2)