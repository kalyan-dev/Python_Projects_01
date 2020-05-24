# - create a list of numbers and select all the numbers that are divisible by 4 or 5; using filter()


def divisible_by(n):
    if n % 4 == 0 or n % 5 == 0:
        return True
    return False


numbers = [12,121,4324,4321,321,5436,34,34345,643,525,10,6568]

for n in filter(divisible_by,numbers):
    print(n, end=' ')
    # pass


# - create a filter to select strings that contain more than 5 characters;

def big_string(s):
    return len(s) > 5


strings = ["how are you", "stay home", "hi", "bye", "name", "cool", "Keep going"]

for s in filter(big_string, strings):
    print(s)
    # pass


# - create a filter to select prime numbers;

def is_prime_number(num):
    flag = True
    for n in range(2,num//2 + 1):
        if num % n == 0:
            flag = False
            break
    return flag


for n in filter(is_prime_number ,range(2,100)):
    print(n, end=' ')


# sorted() example

print("\n-------Sorted Examples---------")
numbers = [12,121,4324,4321,321,5436,34,34345,643,525,10,6568]
print(numbers)
print(sorted(numbers,key=divisible_by,reverse=True))
print(sorted(numbers))

strings = ["how are you", "stay home", "hi", "bye", "name", "cool", "Keep going"]
print("as is..",strings)
print("sorted by length..",sorted(strings, key=len))