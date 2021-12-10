import math

loop = True

while loop:
    def triangle(base, height):
        triangleArea = 0.5 * base * height
        print(f"The area of your triangle is {triangleArea}")
        print("")

    def square(heightOrWidth):
        squareArea = heightOrWidth ** 2
        print(f"The area of your square is {squareArea}")
        print("")

    def rectangle(height, width):
        rectangleArea = height * width
        print(f"The area of your rectangle is {rectangleArea}")
        print("")

    def cone(height, radius):
        coneVolume = math.pi * (radius ** 2) * (height / 3)
        print(f"The volume of your cone is: {coneVolume}")
        print("")

    def cylinder(height, radius):
        cylinderVolume = math.pi * (radius ** 2) * height
        print(f"The volume of your cylinder is: {cylinderVolume}")
        print("")


    shape = str(input("Which shape? Triangle (T), Square (S), Rectangle (R), Cone(C), or Cylinder (CY)? ").upper())

    print("")


    if shape == 'T':
        print("To find the triangle's area, enter its height and base.")
        triangleHeight = int(input("Enter the triangle's height: "))
        triangleBase = int(input("Enter the triangle's height: "))
        print("")
        triangle(triangleHeight, triangleBase)

        again = str(input("Would you like to find the area or volume of another shape? (Y/N): ").upper())

        print("")

        if again == "N":
            loop = False
        
        elif again == "Y":
            loop = True
        
        else:
            print("ERROR \n")
            exit()

    elif shape == 'S':
        print("To find the square's area, enter its height or width.")
        squareHeightWidth = int(input("Enter the triangle's height or width: "))
        print("")
        square(squareHeightWidth)

        again = str(input("Would you like to find the area or volume of another shape? (Y/N): ").upper())

        print("")

        if again == "N":
            loop = False
        
        elif again == "Y":
            loop = True
        
        else:
            print("ERROR \n")
            exit()

    elif shape == 'R':
        print("To find the area of your rectangle, enter its height and width.")
        rectangleHeight = int(input("Enter the rectangle's height: "))
        rectangleWidth = int(input("Enter your rectangle's width: "))
        print("")
        rectangle(rectangleHeight, rectangleWidth)

        again = str(input("Would you like to find the area or volume of another shape? (Y/N): ").upper())

        print("")

        if again == "N":
            loop = False
        
        elif again == "Y":
            loop = True
        
        else:
            print("ERROR \n")
            exit()

    elif shape == 'C':
        print("To find the volume of your cone, enter its height and radius.")
        coneHeight = int(input("Enter the cone's height: "))
        coneRadius = int(input("Enter the cone's radius: "))
        print("")
        cone(coneHeight, coneRadius)

        again = str(input("Would you like to find the area or volume of another shape? (Y/N): ").upper())

        print("")

        if again == "N":
            loop = False

        elif again == "Y":
            loop = True
        
        else:
            print("ERROR \n")
            exit()

    elif shape == 'CY':
        print("To find the volume of your cylinder, enter its height and radius.")
        cylinderHeight = int(input("Enter the cylinder's height: "))
        cylinderRadius = int(input("Enter the cylinder's radius: "))
        print("")
        cylinder(cylinderHeight, cylinderRadius)

        again = str(input("Would you like to find the area or volume of another shape? (Y/N): ").upper())

        print("")

        if again == "N":
            loop = False
        
        elif again == "Y":
            loop = True
        
        else:
            print("ERROR \n")
            exit()

    else:
        print("ERROR \n")
        exit()