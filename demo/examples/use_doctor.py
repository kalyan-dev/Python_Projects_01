import sys

sys.path.append(r"..\oop")

from doctor import Doctor, ResidentDoctor, Consultant, Surgeon

# d1 = Doctor("Scott","ENT",7854972579)
# print(d1.print())

rd1 = ResidentDoctor("Scott","ENT",7854972579, 100000)
print(rd1.print())

sd1 = Surgeon("Yulia","Gaenacology", 652899552, 150000, 78, 3000)
print(sd1.print())

cd2 = Consultant("Kevin", "Arthopaediac", 564875594, 45, 2400)
print(cd2.print())
# cd1 = Consultant("Jovy","Cardiac", 9854928853, 20, 4000)
# print(cd1.print())



