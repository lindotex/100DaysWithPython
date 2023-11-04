# Conditional Statements, Logical Operators, Code Blocks and Scope.

If/Else statement:

```python
    if condition:
        do this
    else:
        do that
```

example:

```python
# Controling the level of water.
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")
```

## Operators

<table>
    <thead>
        <tr>
            <th>Operator</th>
            <th>Meaning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>></td>
            <td>Greater than</td>
        </tr>
        <tr>
            <td><</td>
            <td>Smaler than</td>
        </tr>
        <tr>
            <td>>=</td>
            <td>Greater than or equal</td>
        </tr>
        <tr>
            <td><=</td>
            <td>Smaler than or equal</td>
        </tr>
        <tr>
            <td>==</td>
            <td>Equal to</td>
        </tr>
        <tr>
            <td>=!</td>
            <td>Not equal to</td>
        </tr>
    </tbody>

<table>

## Modular (checking if a division is Odd or Even)

```python
#We can use the operator "%" (Modular)

num = 5 / 2 # It will return 2.5
num = 5 % 2 # It will return 1, the rest of the division
```

## Nested if/else statements

```python
water_level = 100
can_swim = true
if water_level > 80:
    print("Swim")
    if can_swim == true:
        print("I am swiming!")
    else:
        print("I don't know how to swim! HELP!!")
else:
    print("Walk")
```

## Elif statements

A nested statements used when you have a decision block with more than two options with diferent outcomes.

```python
if something:
    #action
elif something_else:
    #action 2
else something_more:
    #action 3
```

Example with BMI calculator:

```python
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
```

## Multiple If Statements:

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
age = int(input("How old are you?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    if age <= 12:
        print("Child, pay $5.00 to enter")
        bill = 5
    elif age < 18:
        print("Youth, pay $7.00 to enter.")
        bill = 7
    else:
        print("Adult, pay $12.00 to enter.")
        bill = 12
    whants_photo = bool(input("Do you wanna photo taken? Y or N"))

    ## ADDING AN CONDITION INNER ANOTHER ONE:

    if whants_photo == "y":
        bill = bill + 3
        print("Your Photo has been taken, your Bill is ${bill}")
    else:
        print("Your Photo hasn't been taken, your Bill is ${bill}")

    ## ADDING AN CONDITION INNER ANOTHER ONE:

else:
    print("You can not ride the rollercoaster yet...")
```
