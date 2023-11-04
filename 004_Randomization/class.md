# Lesson 4

## Randomization Module

Python uses "Mersenne Twister", a math procedure to generate random numbers based on period lenght is chosen to be a Marsenne prime.
check <a href="https://en.wikipedia.org/wiki/Mersenne_Twister"> this article </a> for more information.

To use the random expression in python, you must call it, importing at your archive:

```python
import random

random_interger = random.randint(1,10) #will generate a number between 1 and 10.
print(random_interger)

random_float = random.random() #Will generate a float number between 0 and 1.
print(random_float)
```

## Offset and Appending itens to List (data structure):

Lists are generated in python using the notation below:

```python
fruits = ["apple","pear", "grape"]
```

they are inside brackets and separeted by comas.

## OFFSET:

A List doesn't start at the position 1... it starts at 0! And all the following itens of a list, is counted after its orign... in this sense, the second item of a list, has an offset (from the orign) of 1. the fouth item, has an offset of 3. and so on...

```python
states_of_america = ["Delaware", "Pensilvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[1]) # This will return the value: "Pensilvania."
```

you can also get itens at oposite direction (the last to the first), if you go to the negative value.

```python
states_of_america = ["Delaware", "Pensilvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[-1]) # This will return the value: "Connecticut."
```

You can also, set a new value for any item on a list, simply calling for its value and replacing it:

```python
states_of_america = ["Delaware", "Pensilvania", "New Jersey", "Georgia", "Connecticut"]
states_of_america[-1] = "Conecuticuti" # This will replace the value "Connecticut" for "Conecuticuti".
```

## Append:

this function will add another item at the end of the list:

```python
states_of_america.append("Colorado")
# This will add "Colorado" as a new Item at the end of the list.
```

## Extend:

this function will add a set of itens at the end of the list:

```python
states_of_america.extend(["A", "B", "C"])
# This will add "A", "B" and "C" as a new Item at the end of the list.
```
