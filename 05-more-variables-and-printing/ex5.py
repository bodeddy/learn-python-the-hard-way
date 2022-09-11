name = "Zed A. Shaw"
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky. Try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

inch_cent = height * 2.54
print(f"{height} inches in centimeters is {inch_cent}.")

pound_kilo = weight / 2.205
print(f"{weight} pounds in kilograms is {pound_kilo}.")
