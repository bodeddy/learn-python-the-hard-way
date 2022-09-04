# This variable contains an integer
cars = 100

# This variable contains an integer
space_in_a_car = 4

# As does this one
drivers = 30

# And so does this one
passengers = 90

# This variable contains two previously delcared variables, as well as a mathematical operator
cars_not_driven = cars - drivers

# This variable is simply another variable. I wonder if this is a mistake? Why create a new variable for a variable that already exists?
cars_driven = drivers

# This variable contains two other variables and a mathematical operator
carpool_capacity = cars_driven * space_in_a_car

# This variable contains two other variables and a mathematical operator
average_passengers_per_car = passengers / cars_driven

# These print function print strings and also variables. For the variables, what will show when the code is run is what's stored inside the variable, rather than the variable name. 
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")