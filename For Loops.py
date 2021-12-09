for x in range(10):
    print(x)

print("")

for x in range(2, 10):
    print(x)

print("")

for x in range(2, 100, 3):
    print(x)

print("")

for x in range(2, 10, 3):
    print(x)

print("")

for x in range(10):
    print(x)
else:
    print("Finished counting!")

print("")

for x in range(10):
    if x == 3: break
    print(x)
else:
    print("Finished counting!")

print("")

people1 = ["Joseph", "Alma", "Siamak"]
for x in people1:
    print(x)
    if x == "Siamak":
        break

print("")

people2 = ["Joseph", "Alma", "Siamak"]
for x in people2:
    if x == "Siamak":
        break
    print(x)

print("")

people3 = ["Joseph", "Alma", "Siamak"]
for x in people3:
    if x == "Alma":
        continue
    print(x)
