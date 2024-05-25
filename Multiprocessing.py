import time
import multiprocessing
import multiprocessing.process

def calculate_square(arr, result, sum1):
    for idx, n in enumerate(arr):
        result[idx] = n*n

    sum1.value = sum(result)
    print('square result: ' + str(result[:]))
    print('square sum: ' + str(sum1.value))

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,7,8,9]

    result = multiprocessing.Array('i', len(arr))
    sum = multiprocessing.Value('i')
    p1 = multiprocessing.Process(target=calculate_square, args=(arr, result, sum))

    p1.start()
    p1.join()

    print('Global result: ' + str(result[:]))
    print('Global sum: ' + str(sum.value))
    print('Done!')