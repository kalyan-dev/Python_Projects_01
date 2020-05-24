
with open("marks_list.txt","rt") as f:

    students = {}
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = parts[1:]
        # students[name] = sum(map(int,marks))

        # remove spaces from marks, ignore blank marks;
        students[name] = sum(map(lambda v: int(v.strip()) if v.strip().isdigit() else 0 , marks))

    for name, marks in sorted(students.items()):
        print(f"{name:10}  {marks:4}")