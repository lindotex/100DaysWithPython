# Day 6 | Funcions, code blocks and While Loops

## Functions:

Some kwown functions that we've been using at the course:

- print( ) : Prints something from code to screen.
- len() : Returs the sum of characters in a string.
- int(): Turns the input on a interger
  ...

we can define our own function using the expression below:

```python
def my_function():
    # Do this
    # Do that
    # Finally do this...

# Calling the fuction
my_function()
```

## While Loops:

So far, we have been using the method "for" to complete some exercices with repetitions. But "for" has its own limitations.
We learnt that we can use "for" in two different ways:

```python
# first
# to run a set of list
for item in item_list:
    print(item)

# second
# to run in a certain range of times
count = 0
for item in range(1, x + 1):
    count += item
```

but with While Loops, we canrun troughout some operations until we reach the conditions determined at the while function (until it became TRUE).

ex:

```python
count = 10
while count > 0:
    jump()
    count -= 1

# it will execute the function jump() for a set of 10 times.
```
