import sys

sys.path.append(r"..\oop")
from person import Person




pl = []
pl.append(Person("Scott",35))
pl.append(Person("Jessie",31))
pl.append(Person("Daniel",45))
pl.append(Person("Nancy",23))
pl.append(Person("Sarah",15))
pl.append(Person("Robin",29))



# for p in sorted(pl, key=lambda v : str(v.age)):
#     print(p.print())
#

for p in sorted(pl, key=lambda v : v.name):
    print(p.print() + "[" + p.type + "]")


def find_person(search_person):
    for p in pl:
        if search_person == p:
            return "Person found: " + p.print()
    return "person not found"


search_person = Person("Robin", 29)
print(find_person(search_person), "[" + search_person.type + "]")