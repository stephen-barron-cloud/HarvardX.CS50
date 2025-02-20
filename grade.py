score = int(input("what is the score? "))

# Option 1
if score >= 90 and score <=100:
    grade = "A"
elif score >= 80 and score <90:
    grade = "B"
elif score >= 70 and score <80:
    grade = "C"
elif score >= 60 and score <70:
    grade = "D"
elif score >= 0 and score <60:
    grade = "F"
else:
    grade = "Rocketship"

print("Grade: ",grade)
print()

#option 2
if  90 <= score <=100:
    grade = "A"
elif 80  <= score <90:
    grade = "B"
elif 70  <= score <80:
    grade = "C"
elif 60  <= score <70:
    grade = "D"
elif 0  <= score <60:
    grade = "F"
else:
    grade = "Rocketship"

print("Grade: ",grade)
print()

#option 3
if  score >= 90: 
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ",grade)
print()