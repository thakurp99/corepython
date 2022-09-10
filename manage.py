import emp,work
from emp import *
from work import *


class Mgment(Work):
    def __init__(self,place,manager,staff):
        self.place = place
        self.manager = manager
        self.staff = staff
        super(Mgment, self).__init__(b_loan="2 l",p_loan="3 l",h_loan="5l")
    def getPlace(self):
        return self.place

    def getManage(self):
        return self.manager

    def getStaff(self):
        return self.staff

abc = Mgment("Indore",2,5)
print("Name =",abc.getName())
print("ID = ",abc.getId())
print("Salary =",abc.getSal())
print("B_loan =",abc.getBloan())
print("H_loan =",abc.getHloan())
print("P_loan =",abc.getPloan())
print("Manager =",abc.getManage())
print("Place =",abc.getPlace())
print("Staff =",abc.getStaff())

