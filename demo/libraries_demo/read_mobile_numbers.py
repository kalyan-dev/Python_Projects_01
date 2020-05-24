# - COntacts.txt contains ..(Name,Mobileno) in every line
# - ignore the lines where mobile number is not present
# - ignore the invalid entries;
# - Mobile numeber validation[10 digits, ]

f = open("contacts.txt","rt")

contacts = {}

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2 \
            or parts[1].strip().__len__() < 10 \
            or parts[1].strip().__len__() > 10 \
            or not parts[1].strip().isdigit():
        continue
    contacts[parts[0]] = parts[1].strip()
f.close()

for name,no in contacts.items():
    print(f"{name:15} - {no:12}")