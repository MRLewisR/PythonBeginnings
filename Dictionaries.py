#Dictionaries are key-value pairs
noises = {
    "cow" : "moo",
    "sheep" : "baaa"
} #'cow' is key, 'moo' is value. Similarly, 'sheep' is key, 'baaa' is value

print(noises["cow"])

noises["chicken"] = "cluck" #Add data into the dictionary
print(noises["chicken"])

noises["sheep"] = "meh" #Changes the value associated with the 'Sheep' key
print(noises)

print(noises.keys()) #Prints keys
print(noises.values()) #Prints values
print(noises.items()) #Prints keys and values

if "moo" in noises.values():
    print(True)

if "moo" in noises.keys(): #Will not be true since 'moo' is a value, not a key
    print(True)

words = {"hello" : "hola", "thank-you": "gracias"}

print(words.get("hello")) #Returns the value of the specified key

words.pop("hello") #Removes the 'hello' key, and its related valued ('hola')
print(words)

words.update({"beer" : "cerveza", "hello" : "ey"}) #Adds these key-value pairs to the dictionary
print(words)