score = eval(input("Enter your score between 0% and 100%: "))

if score >= 90.0:
    grade = "A"
elif score >= 80.0:
    grade = "B"
elif score >= 70.0:
    grade = "C"
elif score >= 60.0:
    grade = "D"
else:
    grade = "F"

print(f"Your grade for your {score} is {grade}")