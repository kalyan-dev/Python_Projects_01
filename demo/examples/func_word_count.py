#  create a function that takes a string and returns the number of words the string has;
# there can be multiple spaces in between the words;


def word_count(txt):
    words = []
    words2 =[]
    words = txt.split(sep=' ')
    for i in range(0,len(words)):
        if words[i] != '':
            words2.append(words[i])
    print(words2)
    return len(words2)


def word_count2(txt):
    words = []
    words2 =[]
    words = txt.split(sep=' ')
    for w in words:
        if w != '':
            words2.append(w)
    print(words2)
    return len(words2)


# st = input("Enter a string:")

st = "have a   nice    day. stay home      and  stay   safe."

print(f"you have entered {word_count2(st)} words")