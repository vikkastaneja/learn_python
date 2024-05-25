import time
import multiprocessing
import multiprocessing.process
# We will create two processes doing two different operation on the same set of data
result = []
def calculate_square(arr):
    for n in arr:
        result.append(n*n)

    print('square result: ' + str(result))


def calculate_cube(arr):
    for n in arr:
        result.append(n*n*n)

    print('cube result: ' + str(result))

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,7,8,9]
    p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Global result: ' + str(result))
    print('Done!')