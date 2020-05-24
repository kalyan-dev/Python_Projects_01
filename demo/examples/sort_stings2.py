# Accept names from user until END is given, and display them in sorted order;

inputs = []
while True:
    s = input("Enter a string(enter END to stop)")
    if s.lower() != "end":
        inputs.append(s)
    else:
        break
print(inputs)

