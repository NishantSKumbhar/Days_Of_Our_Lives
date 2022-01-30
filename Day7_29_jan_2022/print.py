"""
@author : Nishant Sanjay Kumbhar
@goal : print works
"""


class Date:
    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        str_obj = str("{}/{}/{}".format(self.dd, self.mm, self.yy))
        return str_obj


d1 = Date(12, 3, 2002)
print(d1)
print(d1.__str__())
print(Date.__str__(d1))
