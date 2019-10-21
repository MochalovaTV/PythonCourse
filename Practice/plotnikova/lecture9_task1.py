import multiprocessing
import threading
import time

def find_primes(n, start=3):
    arr=list(range(start, n+1))
    for key, i in enumerate(arr):
        for j in range (2,i):
            if i % j == 0:
                arr[key]=0
                break
    return print([c for c in arr if c>0])

def fun1():
    start = time.time()
    a = [[10000], [20000, 10001], [30000, 20001]]
    for i in range(3):
        my_thread = threading.Thread(target=find_primes, args=(a[i]))
        my_thread.start()
        my_thread.join()

    for p in threading.enumerate():
        if p is threading.main_thread():
            continue
        p.join()

    print('Время вычислений для 3 потоков: {}'.format(time.time() - start))

def fun2():
    start = time.time()
    find_primes(30000)
    print('Общее время вычислений без потоков: {}'.format(time.time() - start))

def fun3():
    start = time.time()
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001,))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('Общее время вычислений три процесса: {}'.format(time.time() - start))

if __name__ == '__main__':
    fun1()
    fun2()
    fun3()