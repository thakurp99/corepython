import emp
from emp import *

class Work(Emp):
    def __init__(self,b_loan,h_loan,p_loan):
        self.b_loan = b_loan
        self.h_loan = h_loan
        self.p_loan = p_loan
        super(Work, self).__init__(ename="Ram",eid=101,sal=20000)

    def getBloan(self):
        return self.b_loan


    def getHloan(self):
        return self.h_loan

    def getPloan(self):
        return self.p_loan


