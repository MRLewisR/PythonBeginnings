fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

print("")

for number in range(5):
    print(number)

print("")

for char in "Hello World": #Prints every letter
    print(char)

print("")

for char in "Hello World, it's a good day".split(): #Prints each word separately
    print(char)

print("")

helloWorldString = "Today is a great day, Hello World"

for char in helloWorldString.split():
    print(char)


print("")

dictionary = {"Key": "Value", "NewKey" : "NewValue"}

for value in dictionary.items():
    print(value)

for value in dictionary.keys():
    print(value)

for value in dictionary.values():
    print(value)

print("")

result = []

for x in range(5):
    result.append(x + 1)
    print(result)
print(result)

print("")

for i in range(10):
    if i == 5:
        continue
    print(i)

print("")

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i * j)

print("")

for i in range(5, 11):
    print(i)