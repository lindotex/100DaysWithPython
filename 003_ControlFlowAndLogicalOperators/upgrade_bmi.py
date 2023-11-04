# BMI v.2
# Calculate the BMI and Show the user what band o wheigh they are.

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
text = f"Your current BMI is: {bmi_as_int}"

# Showing the results to the user.
if bmi_as_int <= 18.5:
    print(f"{text}")
    print("You are Underwheight! Take Care!")
elif bmi_as_int <= 24.9:
    print(f"{text}")
    print("You are on your perfect wheight! Congratulations!")
elif bmi_as_int <= 29.9:
    print(f"{text}")
    print("You are overwheight! Let get a small diet!")
elif bmi_as_int <= 34.9:
    print(f"{text}")
    print("You are Obese! Let get a small diet, and a Gym!")
elif bmi_as_int <= 39.9:
    print(f"{text}")
    print("You are Obese II ! Let get a small diet, and a Gym!")
else:
    print(f"{text}")
    print("You are Obese III ! Let get a Treatment.")