import time
import multiprocessing
import multiprocessing.process
# We will create two processes doing two different operation on the same set of data

def calculate_square(arr):
    for n in arr:
        time.sleep(6)
        print(n*n)

def calculate_cube(arr):
    for n in arr:
        time.sleep(4)
        print(n*n*n)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,7,8,9,4,2,4545464,34343,66743,32325667,677443,3346677,33453353,34366,343577,3345,88,4]
    p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!')