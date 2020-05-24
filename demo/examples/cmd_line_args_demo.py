# to find GCD of Two Numbers


import sys

# a = float(input(" Please Enter the First Value a: "))
# b = float(input(" Please Enter the Second Value b: "))

a = int(sys.argv[1])
b = int(sys.argv[2])

i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        gcd = i
    i = i + 1

print("\n GCD of {0} and {1} = {2}".format(a, b, gcd))



