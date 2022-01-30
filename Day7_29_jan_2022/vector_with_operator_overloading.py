"""
@author : Nishant Sanjay Kumbhar
@goal : implement the vector addition, multiplication,.....using operator overloading
"""


class Vector:
    def __init__(self, a: float, b: float):
        """
        This is Vector class Constructor
        :param a: first parameter of vector
        :param b: second parameter of vector
        """
        self.a = a
        self.b = b
        
    def addition_of_vector(self, other):
        """
        This method is used to add two vectors
        :param self : this is v1 vector object
        :param other : this is v2 vector object
        """
        add_1 = self.a + other.a
        add_2 = self.b + other.b
        send = Vector(add_1, add_2)
        return send
     
    def substractiontion_of_vector(self, other):
        """
        This method is used to substract two vectors
        :param self : this is v1 vector object
        :param other : this is v2 vector object
        """
        sub_1 = self.a - other.a
        sub_2 = self.b - other.b
        send = Vector(sub_1, sub_2)
        return send

    def multiplication_of_vector(self, other):
        """
        This method is used to multiply the vector
        :param self: v1 object
        :param other: v2 object
        """
        mul = (self.a*other.a) + (self.b*other.b)
        return mul
        
    def __add__(self, other):
        """
        This method is used to add two vectors
        :param self : this is v1 vector object
        :param other : this is v2 vector object
        """
        add_1 = self.a + other.a
        add_2 = self.b + other.b
        send = Vector(add_1, add_2)
        return send
    
    def __sub__(self, other):
        """
        This method is used to substract two vectors
        :param self : this is v1 vector object
        :param other : this is v2 vector object
        """
        sub_1 = self.a - other.a
        sub_2 = self.b - other.b
        send = Vector(sub_1, sub_2)
        return send
        
    def __mul__(self, other):
        """
        This method is used to multiply the vector
        :param self: v1 object
        :param other: v2 object
        """
        mul = (self.a*other.a) + (self.b*other.b)
        return mul

    def show(self, name):
        print("{} : {:.2f} + {:.2f}".format(name, self.a, self.b))
        
 
print("Without Operator Overloading")
v1 = Vector(-5.6, 9.4)
v1.show("v1")
v2 = Vector(3.4, 5.7)
v2.show("v2")
addi = v1.addition_of_vector(v2)
addi.show("addition")
subs = v1.substractiontion_of_vector(v2)
subs.show("Substraction")
multi = v1.multiplication_of_vector(v2)
print("multiplication : {:.2f}".format(multi))
print("With Operator Overloading")
a = v1 + v2
a.show("opera addition")
s = v1 - v2
s.show("opera subtraction")
m = v1 * v2
print("opera multiplication : {:.2f}".format(m))


"""
v1 + v2                     (MATHEMATICAL SYNTAX) 
CONVERTS 
v1.__add__(v2)              (OOP PROGRAMMER SYNTAX )  
CONVERTS 
Vector.__add__(v1, v2)    (PROCEDURAL PROGRAMMER SYNTAX)
"""