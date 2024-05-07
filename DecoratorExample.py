import time

# in this file, we will create an example where we will calculate time spent by running functions, using decorators - meaning there will be decorator to perform the timing function and the functions that we want to get timed, will annotate - this functionality is called decoration.
# This is a decorator function that has a wrapper of the functions to be timed.
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'took', str((end-start) * 1000), 'ms')
        return result
    return wrapper

@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)

    return result

@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)

    return result

print(cal_square([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(cal_cube([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))