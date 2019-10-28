import time


def find_primes(end, start):
    lst =[]
    for n in range(start, end):
        x = True
        for i in range(2, n):
            if n % i == 0:
                x = False
        if x:
            lst.append(n)
    return lst


start_time = time.time()
y = find_primes(10000, 3)
y_1 = find_primes(20000, 10001)
y_2 = find_primes(30000, 20001)
print(y)
print(y_1)
print(y_2)
print(time.time() - start_time)

