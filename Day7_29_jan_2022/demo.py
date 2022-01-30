"""
@author: Yogeshwar
@goal: To implement array class with operator loading support
"""

import sys


class Array:
    def __init__(self, size_of_array: int):
        if type(size_of_array) != int:
            print("Bad type for array size")
            sys.exit(-1)
        if size_of_array < 0:
            print("Bad size for array size")
            sys.exit(-1)
        self.size = size_of_array
        self.internal_list = []
        for i in range(self.size):
            self.internal_list.append(0)

    def __str__(self):
        return str(self.internal_list)

    def __len__(self):
        return self.size

    def __setitem__(self, index, value):
        self.internal_list[index] = value

    def __getitem__(self, index):
        return self.internal_list[index]

    def __add__(self, other):
        summation_A = Array(self.size + other.size)
        summation_A.internal_list = self.internal_list + other.internal_list
        return summation_A

    def __mul__(self, n: int):
        mul_A = Array(n * self.size)
        mul_A.internal_list = self.internal_list * n
        return mul_A

#-------------------------------------------------------------------
# CLIENT SIDE
A1 = Array(5) # Array.__init__(new object of Array, 5)
print("A1:", A1)
print("len(A1):", len(A1))

# index 0 <- 100, index 1 <- 200, index 2 <- 300
# index 3 <- 400, index 4 <- 500
for i in range(len(A1)):
    A1[i] = (i+1) * 100 # Array.__setitem__(A1, i, (i+1) * 100)

for i in range(len(A1)):
    print("A1[", i, "]:", A1[i]) # Array.__getitem__(A1, i)

print("A1:", A1)
print("len(A1):", len(A1))
#-------------------------------------------------------------------
A2 = Array(6)
print("BEFORE A2:", A2)
# index 0 <- 5
# index 1 <- 10
# index 2 <- 15
# index 3 <- 20
# index 4 <- 25
# index 5 <- 30
for i in range(len(A2)):
    A2[i] = (i+1)*5
print("AFTER A2:", A2)


A3 = Array(8)
print("BEFORE A3:", A3)
# index 0 <- 100
# index 1 <- 200
# index 2 <- 300
# index 3 <- 400
# index 4 <- 500
# index 5 <- 600
# index 6 <- 700
# index 7 <- 800
for i in range(len(A3)):
    A3[i] = (i+1) * 100
print("AFTER A3:", A3)

A4 = A2 + A3 # A4 == [5, 10, 15, 20, 25, 30, 100, 200, 300, 400, 500, 600, 700]
A5 = A2 * 3  # A5 == [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]
print("A4:", A4)
print("A5:", A5)
