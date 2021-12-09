lbs = eval(input("Enter a number in lbs: "))
kg = lbs * 0.45359237

inches = eval(input("Enter height in inches: "))
metres = inches * 0.0254

BMI = kg / (metres**2)

print("BMI is", BMI)