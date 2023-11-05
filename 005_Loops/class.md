# Lesson 5 : Loops

## For Loop

```python
for item in list_of_items:
    #do something
```

for every item listed at list_of_items, your code will do an specific task.
for example:

```python
total_height = 0
for height in student_heights:
    total_height += height

print(f"Total Height: "{total_height})
```

in this scenario, your code will run throughout all **"student_heights"** one by one, and sum every one of it with the next one, and print the sum at the end.
