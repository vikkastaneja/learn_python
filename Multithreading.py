import time
import threading

def square(numbers):
    for number in numbers:
        time.sleep(0.1)
        print('square of', number, 'is', number*number)


def cube(numbers):
    for number in numbers:
        time.sleep(0.1)
        print('cube of', number,'is', number*number*number)

numbers=[2,3,4,5,6,7,8,9]
t1 = time.time()
square(numbers=numbers)
cube(numbers=numbers)
print('Time take to run in sequence is', time.time()-t1)

t2 = time.time()
thread1 = threading.Thread(target=square, args=(numbers,))
thread2 = threading.Thread(target=cube, args=(numbers,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Time taken when running in threads:', time.time()-t2)