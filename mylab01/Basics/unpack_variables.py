
# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.

# variable assignment
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, date = data
print("Shares", shares)
print("price", price)
print("Date", date)

# string
s = 'HEllo'
a,b,c,d,e = s
print (a,b,c,d,e)

# tuple
p = (5,6)
x,y = p
print(x)
print(y)

# list
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name,shares,price,date = data
print(name, shares, price, date)

