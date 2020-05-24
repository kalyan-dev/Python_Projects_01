class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        return self.name + " " + str(self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @property
    def type(self):
        if self.age <= 12:
            return "Child"
        elif self.age <= 30:
            return "Young"
        elif self.age <= 50:
            return "MiddleAge"
        else:
            return "OldAge"
