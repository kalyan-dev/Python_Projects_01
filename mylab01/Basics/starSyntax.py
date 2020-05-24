# unpacking iterables of unknown or arbitrary
# length.


def drop_first_last(items):
    first, *middle, last = items
    return sum(middle)


testItems = [2, 3, 4, 5, 6, 7]
print(drop_first_last(testItems))

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(phone_numbers)

# It’s worth noting that the phone_numbers variable will always be a list

*allButOne, last = testItems
print(allButOne)

# It is worth noting that the star syntax can be especially useful when iterating over a
# sequence of tuples of varying length.


def processrecords(head, *params):
    if head == "one":
        print("one: ", params)
    if head == "two":
        print("two", params)


records = [
    ("one", 3, 4, 4),
    ("one", 2, 7),
    ("two", 62, 452, 255, 89)
]

for r in records:
    head, *params = r
    processrecords(head, *params)


# line splitting by delimiter

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(fields)

# throwaway variable
_, *fields, _, sh = line.split(':')
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(year)

tt = (4, 5, 6, 7, 42, 452, 52)
h, *t = tt
print(t)
