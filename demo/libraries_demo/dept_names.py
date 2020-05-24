
with open("dept_names.txt","rt") as f:
    dept_employees = {}

    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2 or parts[1].strip().__len__() < 1:
            continue
        dept = parts[0]
        employee = parts[1].strip()

        # To store the employees as a List
        # if dept in dept_employees:
        #     dept_employees[dept].append(employee)
        # else:
        #     dept_employees[dept] = [employee]

        # To store the employees as a String
        if dept in dept_employees:
            dept_employees[dept] += ", " + employee
        else:
            dept_employees[dept] = employee

# for d,el in dept_employees.items():
#     print(d,el)

for d,el in sorted(dept_employees.items(), key=lambda v:int(v[0])):
    print(f"{d:4} - {el}")


# write the output in a file
with open("dept_names_output.txt","wt") as f:
    for d, el in sorted(dept_employees.items(), key=lambda v: int(v[0])):
        f.write(f"{d:4} - {el}" + "\n")

