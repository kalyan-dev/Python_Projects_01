
# The heapq module has two functions—nlargest() and nsmallest()

import heapq

Nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(2,Nums))
# print(heapq.nsmallest(2,Nums))

# print(sorted(Nums))
# print(sorted(Nums)[:3])
# print(sorted(Nums)[:-3])


h = list(Nums)
heapq.heapify(h)
print(h)
print(heapq.heappop(h))
print(h)







portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)