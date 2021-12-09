numbers = ["2423", "359", "9983", "35", "4"]

print(numbers[:2]) #Prints the first two items in the list
print(numbers[-1]) #This will always give you the final item in the list. Essentially, with -1, it loops around to the end of the list
print(numbers[-2]) #This will give you the second the last item in the list

numbers[1] = "8274"

print(numbers)

del numbers[0]

print(numbers)

if "35" in numbers:
    print(True)

numbers.append("176532")
print(numbers)

numbers.remove("4") #Name the item, can't use the index
print(numbers)

numbers.pop(0) #Removes the item at the specified index
print(numbers)

numbers.insert(1, "999") #Add a value into the list, specify the position and the value/item
print(numbers)

numbers.extend(["23432", "266"]) #Adds mutiple items to the end of the list
print(numbers)

#Another way of extending:
numbers2 = ["3320", "3344344"]
numbers.extend(numbers2)
print(numbers)

print("35 is at index:", numbers.index("35")) #Tells you the index of the item

numbers.reverse()
print(numbers)

print(", ".join(numbers)) #Separates the items by a comma and a space