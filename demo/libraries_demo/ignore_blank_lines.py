
while True:
    fname = input("Enter the filename:")

    try:
        with open(fname,"rt") as f:
            for line in f.readlines():
                # print(line.strip().__len__())
                if line.strip().__len__() > 0:
                    print(line, end=">>")
        break
    except Exception as e:
        print(f"File {fname} not found. Please enter a valid filename.")

