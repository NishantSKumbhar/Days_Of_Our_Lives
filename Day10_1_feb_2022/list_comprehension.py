l = [x for x in range(1, 10)]
print(l)

x = '*' * 30
print(x)

l = [x**2 for x in range(1, 10)]
print(l)

print(x)

l = [x for x in range(1, 10) if x % 2 == 0]
print(l)

print(x)

l = [x ** 2 for x in range(1, 10) if x % 2 == 0]
print(l)

print(x)

l = [(x,y) for x in range(1, 11) for y in range(11, 30)]
print(l)

print(x)

l = [x+y for x in range(1, 10) for y in range(11, 20)]
print(l)

print(x)

l = [(x**2, y**3) for x in range(1, 10) for y in range(1, 10)]
print(l)

print(x)

l = [(x**2 + y**3) for x in range(1, 10) for y in range(1, 10)]
print(l)

print(x)

l = [(x**2, y**3) for x in range(1, 10) if x%2==0 for y in range(1, 10) if y%2==1]
print(l)

print(x)

l = [x**2 + y**3 for x in range(1, 10) if x % 2 == 0 for y in range(1, 10) if y % 2 == 1]
print(l)

print(x)

# apply condition on result
l = [x for x in range(1, 10)]
print(l)

print(x)

l = [x for x in range(1, 10) if x > 5]
print(l)
print(x)

l = [x**2 for x in range(1, 10) if x**2 > 10]
print(l)
print(x)

l = [(x**2, y**3) for x in range(1, 5) if x**2 > 8 for y in range(1, 10) if y**3 > 9 ]
print(l)
print(x)

l = [(x,y) for x in range(1, 10) for y in range(1, 100) if x+y > 100]
print(l)
print(x)

l = [()]
