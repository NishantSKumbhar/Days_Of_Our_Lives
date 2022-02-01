def master(a, b, c, d, e, f, g, h, x, y, z):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, x, y, z))


master(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) # Positional Argument

p = '*---*' * 15
print(p)


def master(a, b, c, d, e, f, g, h, x, y, z):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, x, y, z))


master(1, 2, 3, 4, 5, 6, 7, h=8, x=9, y=10, z=11) # in actual parameter if you started to give keyword arg then go tll end.
print(p)


def master(a, b, c, d, e, f, g, h, x, y, z):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, x, y, z))


master(1, 2, 3, 4, 5, 6, 7, h=88, x=99, y=110, z=111)
print(p)


def master(*args): # Extra-Non Keyword Argument
    print("args : {}".format(args))   # it return the tuple of all non-keyword arg
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(args[0], args[1], args[2],
                                                                                               args[3], args[4], args[5],
                                                                                               args[6], args[7], args[8],
                                                                                               args[9], args[10]))


master(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(p)


def master(a, b, c, d, e, *args):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, args[0], args[1], args[2], args[3],
                                                                                               args[4], args[5]))


master(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) # Positional Argument
master(1, 2, 3, 4, 5, *(6, 7, 8, 9, 10, 11)) # Positional Argument
print(p)


def master(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, x=0, y=0, z=0):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, x, y, z))


master(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
master(1, 2, 4)  # if we don't pass argument then by default 0 will print
print(p)


def master(a, b, c, *args, x, y, z):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, args[0], args[1], args[2], args[3], args[4], x, y, z))


master(1, 2, 3, 4, 5, 6, 7, 8, x=9, y=10, z=11)
print(p)


def master(a, b, c, *args, x, y, z):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, args[0], args[1], args[2],
                                                                                               args[3], args[4], x, y, z))


master(1, 2, 3, 4, 5, 6, 7, 8, x=9, y=10, z=11)
print(p)


def master(a, b, c, d, e, f, g, h, x=0, y=0, z=9):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, x, y, z))


master(1, 2, 3, 4, 5, 6, 7, 8)
print(p)


def master(a, b, c, d, e, f, g, h, **kwargs):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, kwargs : {}".format(a, b, c, d, e, f, g, h, kwargs))
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, d, e, f, g, h, kwargs['x'], kwargs['y'], kwargs['z']))


master(1, 2, 3, 4, 5, 6, 7, 8, x=9, y=10, z=11)
print(p)


def master(a, b, c, *args, g, h, **kwargs):
    print("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, g: {}, h: {}, x: {}, y: {}, z: {}".format(a, b, c, args[0], args[1], args[2], g, h, kwargs['x'], kwargs['y'], kwargs['z']))


master(1, 2, 3, 4, 5, 6, g=7, h=8, x=9, y=10, z=11)
master(1, 2, 3, *(4, 5, 6), g=7, h=8, x=9, y=10, z=11)
print(p)
