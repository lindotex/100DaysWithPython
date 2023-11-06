# Calculating the sum of the even numbers from 1 to X, 

#my answer
x = int(input("digit a number from 1 to 1000 to se the sum of its even numbers:"))
even_sum = 0
for number in range(2, x + 1):
   if number % 2 == 0:
        even_sum += number
    
print(f"the total sum is: {even_sum}")

#correct answer
target = int(input("digit a number from 1 to 1000 to se the sum of its even numbers:"))
even_sum = 0
for number in range(2, target + 1, 2):
        even_sum += number
print(even_sum)