import multiprocessing
import multiprocessing.process

def calculate_square(arr, result, sum1, sum_first):
    for idx, n in enumerate(arr):
        result[idx] = n*n
        sum_first.value += n

    sum1.value = sum(result)
    print('square result: ' + str(result[:]))
    print('square sum: ' + str(sum1.value))
    print('sum: ' +  str(sum_first.value))

def calc_sq_queue(arr, q):
    map = {}
    sq_list = []
    sum = 0
    sum_sq = 0
    for n in  arr:
        sum += n
        sq_list.append(n*n)
        sum_sq += n*n

    map['sum'] = sum
    map['square_list'] = sq_list
    map['sq_sum'] = sum_sq
    q.put(map)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11]

    print('input array: ' + str(arr))
    result = multiprocessing.Array('i', len(arr))
    sum_sq = multiprocessing.Value('i')
    sum_first = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=calculate_square, args=(arr, result, sum_sq, sum_first))

    p1.start()
    p1.join()

    print('Global result: ' + str(result[:]))
    print('Global sum: ' + str(sum_first.value))
    print('Global sum square: ' + str(sum_sq.value))

    print('\nTrying queue to communicate between processes...')
    q = multiprocessing.Queue()
    p2 = multiprocessing.Process(target=calc_sq_queue, args=(arr, q))
    p2.start()
    p2.join()
    map = None
    while q.empty() is False:
        map = q.get()
        print('Sum from queue: ' + str(map['sum']))
        print('Square list from queue: ' + str(map['square_list']))
        print('Square sum from queue: ' + str(map['sq_sum']))

    print('Done!')