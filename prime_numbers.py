from concurrent.futures import ThreadPoolExecutor
import math
from time import sleep


def is_prime(num):
    if not num:
        return False
    if num == 1:
        return False
    sqrt_num = int(math.sqrt(num)) + 1
    for divisor in range(2, sqrt_num):
        if num % divisor == 0:
            return False
    return True


def get_sum_of_primes(left, right):
    pool = ThreadPoolExecutor(3)
    futures = [pool.submit(is_prime, num) for num in range(left, right)]
    prime_sum = 0
    for num, future in zip(range(left, right), futures):
        while not future.done():
            sleep(0.1)
        if future.result():
            prime_sum += num
    return prime_sum


if __name__ == "__main__":
    print(get_sum_of_primes(1, 10))
    print(get_sum_of_primes(10000, 100000))
