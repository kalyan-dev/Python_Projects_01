# create a function that takes a string and a character and returns the string by removing the character;
# by default the character = ' '


def remove_char(txt, char=' '):
    return txt.replace(char, '')


string = "create a function that takes a string and a character and returns the string by removing the character"
print(remove_char(string,"a"))

