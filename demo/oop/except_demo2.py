# - Accept numbers from user until zero is given and display SUM of the numbers; handle Invalid Numbers;
# program should not crash, but should continue;


def is_integer(n):
    try:
        return float(n).is_integer()
    except ValueError:
        return False


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return False


nums = []
while True:
    try:
        # n = int(input("Enter a number(0 to End) :"))
        sn = input("Enter a number(0 to End) :")
        if not is_integer_num(sn):
            n = float(sn)
        else:
            n = int(sn)

        if n == 0:
            break
        else:
            nums.append(n)
    except:
        print("You have entered an invalid number. Please enter an Integer.")
        continue

print(f"You have entered {nums}")
print(f"Sum of the numbers = {sum(nums)}")

