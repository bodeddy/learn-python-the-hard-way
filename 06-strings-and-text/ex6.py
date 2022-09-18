# An integer variable with the value of 10
types_of_people = 10

# An f-string variable
x = f"There are {types_of_people} types of people."

# A string variable
binary = "binary"

# Another string variable
do_not = "don't"

# Another f-string variable
# String inside a string
y = f"Those who know {binary} and those who {do_not}."

# A print function that takes the variable x
print(x)

# A print function that takes the variable y
print(y)

# A print function that takes an f-string and the x variable within that f-string
# String inside a string
print(f"I said: {x}")

# A print function that takes an f-string and the y variable within that f-string
# String inside a string
print(f"I also said: '{y}'")

# A boolean variable - I didn't realise variables could take True or False
hilarious = False

#A string variable with {} within it
joke_evaluation = "Isn't that joke so funny?! {}"

# A print function that takes the variable joke_evaluation, a format syntax, and the hilarious variable
print(joke_evaluation.format(hilarious))

# A string variable
w = "This is the left side of..."

# A string variable
e = "a string with a right side."

# A print function that concatenates the variable w and e
print(w + e)
