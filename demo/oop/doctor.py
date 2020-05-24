from abc import ABC,abstractmethod


class Doctor:

    def __init__(self, name, specialization, phone_no):
        self.name = name
        self.specialization = specialization
        self.phone_no = phone_no

    def print(self):
        return self.name + "[" + self.specialization + ", Ph-" + str(self.phone_no) + "]"

    @abstractmethod
    def get_salary(self):
        pass


class ResidentDoctor(Doctor):

    def __init__(self, name, specialization, phone_no, salary):
        super().__init__(name, specialization, phone_no)
        self.salary = salary

    def print(self):
        return super().print() + " Total Salary = " + str(self.get_salary())

    def get_salary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, specialization, phone_no, no_of_visits, charge_per_visit):
        super().__init__(name, specialization, phone_no)
        self.no_of_visits = no_of_visits
        self.charge_per_visit = charge_per_visit

    def get_salary(self):
        return self.no_of_visits * self.charge_per_visit

    def print(self):
        return super().print() + " Total Salary = " + str(self.get_salary())

    @property
    def salary(self):
        return self.get_salary()


class Surgeon(Doctor):

    def __init__(self, name, specialization, phone_no, total_surgery_amount, no_of_visits, charge_per_visit):
        super().__init__(name, specialization, phone_no)
        self.total_surgery_amount = total_surgery_amount
        self.no_of_visits = no_of_visits
        self.charge_per_visit = charge_per_visit

    def get_salary(self):
        return self.total_surgery_amount + self.no_of_visits * self.charge_per_visit

    def print(self):
        return super(Surgeon, self).print() + " Total Salary = " + str(self.get_salary())

    @property
    def salary(self):
        return self.get_salary()



