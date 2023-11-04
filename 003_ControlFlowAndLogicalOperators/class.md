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
