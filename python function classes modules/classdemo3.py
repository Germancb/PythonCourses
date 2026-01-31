class ProgStaff:
    companyName = 'ProgrammingLab'
    def __init__(self, pSalary):
        self.salary = pSalary
    def printInfo(self):
        print( "Company name is ", ProgStaff.companyName)
        print( "Salary is ", self.salary)