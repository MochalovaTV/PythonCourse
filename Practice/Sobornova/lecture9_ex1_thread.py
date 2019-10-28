import time
import threading


def find_primes(end, start):
    lst = []
    for n in range(start, end):
        x = True
        for i in range(2, n):
            if n % i == 0:
                x = False
        if x:
            lst.append(n)
    print(lst)


start_time = time.time()
th_1 = threading.Thread(name='th_1', target=find_primes, args=(10000, 3))
th_2 = threading.Thread(name='th_2', target=find_primes, args=(20000, 10001))
th_3 = threading.Thread(name='th_3', target=find_primes, args=(30000, 20001))
th_1.start()
th_2.start()
th_3.start()
th_1.join()
th_2.join()
th_3.join()
print(time.time() - start_time)
