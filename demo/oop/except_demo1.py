# - Accept numbers from user until zero is given and display SUM of the numbers; handle Invalid Numbers;
# program should not crash, but should continue;


nums = []
while True:
    try:
        n = int(input("Enter a number(0 to End) :"))
        if n == 0:
            break
        else:
            nums.append(n)
    except:
        print("You have entered an invalid number. Please enter an Integer.")
        continue

print(f"You have entered {nums}")
print(f"Sum of the numbers = {sum(nums)}")

