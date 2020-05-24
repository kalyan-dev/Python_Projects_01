

def myfunc(a, b):
  return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ['orange', 'lemon', 'pineapple'])
# print(list(x), type(x))
# l = list(x)
# print(l, type(l))
# print(list(x), type(x))

# doubt..
# after performing list(x), x remains as map; but list(x) does not give data anymore;

# print(tuple(x))
# print(set(x))
# print(type(x))

def fun2(a):
  return a.upper()


x2 = map(fun2, ('apple', 'banana', 'cherry'))
print(x2,list(x2), type(x2))
print(x2,list(x2), type(x2))
