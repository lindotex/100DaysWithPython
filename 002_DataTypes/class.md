# Lesson 2

## DATA TYPES:

- String:
  - "Hello"
- Interger:
  - 1, 2, 3, 4
- Float:
  -1.24, 1.55, 7.245
- Boolean
  - true, false. 1, 0.

## DISCECTING A STRING WITH ARRAY NOTATION:

```python
print("hello"[0])
```

This expression will return the value "h" at the console.

## LOOKING FOR WHAT KIND OF TYPE AN ARGUMENT IS:

```python
type(data)
```

It will show what kind of data type data is presenting.

## CONVERTING DATA TYPES

- converting to String:

```python
str(data)
# It will make your data into a String.
```

- converting to an Interger:

```python
int(data)
# It will make your data into Interger.
```

- converting to an Float:

```python
float(data)
# It will make your data into Float.
```

- Examples:

```python
print(70 + float("100.5"))
# This will print 170.5, as a Float number.

print(str(70) + str(100))
# This will print 70100, as a String.
```

## Mathematical Operators:

```python
    # +  : Plus
    # -  : Minus
    # *  : Multiplication
    # ** : Exponent
    # /  : Division
    # %  : Module (rest of division)
    # // : Float division (The result of the division will be an Interger instead of a float)

    # PEMDAS : Order of priorities in math
        # P : Parentheses
        # E : Exponents
        # M : Multiplication
        # D : Division
        # A : Addition
        # S : Subtraction

```

what would be the result of the expression bellow:

```python
print(3 * 3 + 3 / 3 - 3)
```

the way that it is calculated is aways left to right, but respecting the order of priorities (PEMDAS)

```python
3 * 3 + 3 / 3 - 3
9 + 3 / 3 - 3
9 + 1.0 - 3
10 - 3
7
```

## Round Operator

```python
 round(<value>,<decimals>)
```

## Float Division

```python
num1 = 5 / 2   # Result: 2.5
num2 = 5 // 2  # Result: 2

# the results of both divisions are the same, but using "//" will return only the Interger part of the division.
```

## F-string

```python
score = 0
height = 1.8
isWinning = True
f"Your score is {score} and your height is {height}. You are winning is {isWinning}"
#Using F-string will help you to short a lot of lines of coding.
```
