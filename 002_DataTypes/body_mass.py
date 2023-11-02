### Body Mass Indicator
## Formula:
# BMI=(weight/heigh**2)

# Getting the data from the user.
weight = input()
height = input()

# Converting the inputs into usable data.
weight_as_int = int(weight)
height_as_float = float(height)

# Calculating the value of BMI.
bmi = weight_as_int / (height_as_float ** 2)

# Converting the result into a interger.
bmi_as_int = int(bmi)

# Showing the results to the user.
print(bmi_as_int)