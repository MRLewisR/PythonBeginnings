name = input("Enter your name: ")

if name not in ("root", "admin"):
    print("Welcome", name)
else:
    print("This is not a valid username")