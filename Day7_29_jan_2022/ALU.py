""""
@author : Nishant Sanjay Kumbhar
@goal : As we know that previously vector does not support division so we left with integer that support all types.
"""


class CPA_INT:
    def __init__(self, a_int: int):
        self.a = a_int

    def __add__(self, other):
        adi = self.a + other.a
        addi = CPA_INT(adi)
        return addi

    def __sub__(self, other):
        sub = self.a - other.a
        subs = CPA_INT(sub)
        return subs

    def __mul__(self, other):
        mult = self.a * other.a
        multi = CPA_INT(mult)
        return multi

    def __truediv__(self, other):
        div = self.a / other.a
        divi = CPA_INT(div)
        return divi

    def __floordiv__(self, other):
        flr = self.a // other.a
        flrdiv = CPA_INT(flr)
        return flrdiv

    def __mod__(self, other):
        mo = self.a % other.a
        modi = CPA_INT(mo)
        return modi

    def __pow__(self, other):
        po = self.a ** other.a
        powe = CPA_INT(po)
        return powe

    def __lt__(self, other) -> bool:
        return self.a < other.a

    def __le__(self, other) -> bool:
        return self.a <= other.a

    def __gt__(self, other) -> bool:
        return self.a > other.a

    def __ge__(self, other) -> bool:
        return self.a >= other.a

    def __eq__(self, other):
        return self.a == other.a

    def __ne__(self, other):
        return self.a != other.a

    def show(self, message) -> None:
        print("{} : {:.2f}".format(message, self.a))


int_1 = CPA_INT(8)
int_2 = CPA_INT(5)
addition = int_1 + int_2
addition.show("Addition")
subtraction = int_1 - int_2
subtraction.show("Subtraction")
multiplication = int_1 * int_2
multiplication.show("Multiplication")
division = int_1 / int_2
division.show("Division")
floor_division = int_1 // int_2
floor_division.show("Floor Division")
reminder = int_1 % int_2
reminder.show("Reminder")
power = int_1 ** int_2
power.show("Power")
if int_1 > int_2:
    print("Yes {} is greater than {}".format(int_1.a, int_2.a))
else:
    print("NO {} is not greater than {}".format(int_1.a, int_2.a))

if int_1 < int_2:
    print("Yes {} is less than {}".format(int_1.a, int_2.a))
else:
    print("NO {} is not less than {}".format(int_1.a, int_2.a))

if int_1 >= int_2:
    print("Yes {} is greater than or equal {}".format(int_1.a, int_2.a))
else:
    print("NO {} is not greater than or equal {}".format(int_1.a, int_2.a))

if int_1 <= int_2:
    print("Yes {} is less than or equal {}".format(int_1.a, int_2.a))
else:
    print("NO {} is not less than or equal {}".format(int_1.a, int_2.a))

if int_1 == int_2:
    print("Both are Equal")
elif int_1 != int_2:
    print("Both are Not Equal")
