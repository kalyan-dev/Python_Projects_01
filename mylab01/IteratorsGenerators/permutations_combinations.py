# Iterating Over All Possible Combinations or Permutations

items = ['a','b','c']

from itertools import permutations,combinations,combinations_with_replacement

for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)


for c in combinations(items,2):
    print(c)

for c in combinations_with_replacement(items,2):
    print(c)