import math

radius, length = eval(input("Enter radius then length, separated with a comma: "))
area = radius * radius * math.pi
volume = area * length

print("The radius is: ", radius)
print("The length is", length)
print("The area is", area)
print("The volume is", volume)