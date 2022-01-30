l = [1, 2, 3,4 ,5,6,7,8]
r = reversed(l)
j = []
for i in r:
    j.append(i)

print(j)
j.append(l)
print(j)