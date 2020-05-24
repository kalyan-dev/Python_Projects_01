# - Accept 5 strings from user and display how many of them contain atleast a digit;

count = 0
for i in range(1,6):
    s1 = input("Enter a string:")
    for c in s1:
        if c.isdigit():
            count += 1
            break

print(f"{count} stings contains atleast a digit")