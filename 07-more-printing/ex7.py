# Prints a string
print("Mary had a little lamb.")

# Prints a string and also placeholder text as indicated by the format() function
print("Its fleece was as white as {}.".format("snow"))

# Prints a string
print("And everywhere that Mary went.")

# Prints a string out 10 times, as is instructed by * 10
print("." * 10) # what'd that do? This multiplies . 10 times to give ..........

# The are all variables with a string assigned to them.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Both of these print variables, but the first line includes end=" " which indicates that the following print should follow on the same line.
# watch end = " " at the end. Try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ") # if you remove end=" " then the two print functions display their arguments on different lines. I suppose end=" " behaves the same way /n does.
print(end7 + end8 + end9 + end10 + end11 + end12) 
