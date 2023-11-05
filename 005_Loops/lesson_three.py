# Calculate the highest score:
# Replicating the max() with for loops

### Input a list of students

student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

################################################

score = 0

