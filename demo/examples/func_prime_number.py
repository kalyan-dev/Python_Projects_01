# create a function that takes a number, return True if number is a prime number, otherwise False


def is_prime_number(num):
    flag = True
    for n in range(2,num//2 + 1):
        if num % n == 0:
            flag = False
            break
    return flag


# num = int(input("Enter a Number:"))

num = 13
if is_prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# print(f"{num} {"is" if is_prime_number(num) else "is not"} a prime number")
