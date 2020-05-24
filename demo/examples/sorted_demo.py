# - sort a Dictionary by its values, not by the keys;


dict1 = {"Kalyan":37, "raju":45, "Shweta":26, "monu":14, "Bunny":8, "reetu":68}
dict2 = {"3":"Rajesh", "2":"Anand", "7":"Mahesh", "9":"Pooja", "1":"Dinesh"}

# print(dict1)
# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())


print(sorted(dict1.items(), key=lambda v : v[0].lower()))

dict1 = {"Kalyan":37, "raju":45, "Shweta":26, "monu":14, "Bunny":8, "reetu":68}
print(sorted(dict1.items(), key=lambda v : v[0]))

print(sorted(dict2.items(), key=lambda v : v[0]))


