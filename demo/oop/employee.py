class Employee:

    hra = 15

    def __init__(self, empid, name, salary=0):
        self.empid = empid
        self.name = name
        self.salary = salary

    def print(self):
        return str(self.empid) + " " + self.name + " " + str(self.salary)

    def get_salary(self):
        return self.salary + self.salary * Employee.hra /100

    @classmethod
    def set_hrapct(self,new_hra):
        Employee.hra = new_hra


el = []
el.append(Employee(100,"Raju", 20000))
el.append(Employee(103,"Jenny", 30000))
el.append(Employee(104,"Scott", 24000))
el.append(Employee(105,"Tom", 18000))
el.append(Employee(107,"Nikki", 55000))


for e in el:
    print(e.print())

Employee.set_hrapct(10)
for e in el:
    print(f"{e.name}(EmpID:{e.empid}) is earning a salary of INR {e.get_salary()}")
