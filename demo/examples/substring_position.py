# take 2 strings(main string and substring) from user,
# Display all the positions of the occurrences of the substring in the main string;

# main = input("Enter the main string:")
# sub = input("Enter the substring:")


main = "this is the main string. That is another string"
sub = "is"

ix = 0
while ix != -1:
    print(f"{sub} is found at index -> {main.find(sub,ix)}")
    if main.find(sub,ix) != -1:
        ix = main.find(sub,ix) + 1
    else:
        break
# print(main.find(sub,))
