"""
@author : Nishant Sanjay Kumbhar
@goal: implement array
"""
import sys


class Blue_array:
    def __init__(self, size_of_array: int):
        if size_of_array < 0:
            print("Bad size Type for array ")
            sys.exit(-1)
        if type(size_of_array) != int:
            print("Bad type for size of array")

        self.size = size_of_array
        self.internal_list = []
        for i in range(self.size):
            self.internal_list.append(0)

    def __setitem__(self, key, value):  # set used as [] to set item at LHS
        self.internal_list[key] = value

    def __getitem__(self, key):  # get used as [] to get item as RHS
        return self.internal_list[key]

    def __len__(self):  # len used as len() to get length
        return self.size

    def __str__(self):  # str used as to print direct object
        return str(self.internal_list)

    def __add__(self, other):  # add used to add two arrays
        end_array = Blue_array(self.size + other.size)  # we are assigning the new size for end_array
        end_array.internal_list = self.internal_list + other.internal_list
        return end_array

    def __mul__(self, value):
        multi = Blue_array(self.size * value)
        multi.internal_list = self.internal_list * value
        return multi


a1 = Blue_array(5)
a2 = Blue_array(15)
a3 = Blue_array(21)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

"""
a1.internal_list[0] = 15
a1.internal_list[1] = 16
a1.internal_list[2] = 17
print(a1.__dict__)
"""
a1[0] = 10  # subscript operator is at left -> getitem
# above can be represented as
# a1.__setitem__(index, value)
# Blue_array.__setitem__(a1, i, value)

a1[1] = 20
a1[2] = 30
a2[2] = 22
a2[5] = 55
print("a1 : {}".format(a1.internal_list))
print("a2 : {}".format(a2.internal_list))
print("length of a1 : {}".format(len(a1.internal_list)))
# we want to get elements->
n1 = a1[0]  # subscript operator is at right -> setitem

print("n1 : {}".format(n1))

for i in range(0, 5):
    print(a1[i])

print("length of a1 : {}".format(len(a1)))
print("length of a2 : {}".format(len(a2)))
print("length of a3 : {}".format(len(a3)))

print("a1 : {} \na2 : {}\na3 : {}".format(a1, a2, a3))

# now using above implementation
a7 = Blue_array(3)
for i in range(len(a7)):
    a7[i] = int(input("Enter the Number for {} index :".format(i)))

for i in range(len(a7)):
    print("{}".format(a7[i]))

print(a1)
print(a2)
print(a3)
print(a7)

# using + and *
a9 = a1 + a7
print("addition of a1 + a2 : {}".format(a9))

# if we want to print array -- times
a10 = a9 * 3
print("a10 : {}".format(a10))
