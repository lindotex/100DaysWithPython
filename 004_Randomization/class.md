# Class 4

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
