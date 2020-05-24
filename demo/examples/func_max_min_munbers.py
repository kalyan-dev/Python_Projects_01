# create a function that takes a list of numbers, and returns the smallest and largest values in the collection.


def find_min_max(nums):
    result = {"small": min(nums), "big": max(nums)}
    return result


def find_min_max2(nums):
    result = {}
    small = big = nums[0]
    for n in nums:
        if n > big:
            big = n
        if n < small:
            small = n
    result["small"] = small
    result["big"] = big
    return result


nums = [31,341,41,431,341,41,431,54,42,864,23]
print(find_min_max(nums))
