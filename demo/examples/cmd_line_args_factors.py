
import sys

# This function computes the factor of the argument passed


def get_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

# num = 320


num = int(sys.argv[1])
factors = get_factors(num)
print(f"The factors of {num} are :", factors)

