weight = eval(input("Enter your weight in lbs: "))
height = eval(input("Enter your height in inches: "))

kgPerPound = 0.45359237
metresPerInch = 0.0254

weightInKg = weight * kgPerPound
heightInMetres = height * metresPerInch

bmi = weightInKg / (heightInMetres ** 2)

print("Your BMI is", format(bmi, ".2f"))

#Below 18.5 = Underweight
#Between 18.5 and 24.9 = Healthy
#Between 25.0 and 29.9 = Overweight
#Above 30.0 = Obese

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are at a healthy weight")
elif bmi >= 25.0 and bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")