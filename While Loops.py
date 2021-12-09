i = 1
while i < 6:
    print(i)
    i += 1

print("")

j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

print("")

k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k)

print("")

l = 1
while l < 6:
    print(l)
    l += 1
else:
    print("l is no longer less than 6")