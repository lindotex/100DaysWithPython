# Calculate the highest score:
# Replicating the max() with for loops

### Input a list of students

student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

################################################

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
        #print(high_score)

print(f"The highest score in a class is {high_score}")

