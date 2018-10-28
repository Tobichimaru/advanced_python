import multiprocessing


def odd(curr, end, lock):
    while True:
        if curr.value > end:
            return
        if int(curr.value) % 2:
            lock.acquire()
            print(curr.value)
            curr.value += 1
            lock.release()


def even(curr, end, lock):
    while True:
        if curr.value > end:
            return
        if not int(curr.value) % 2:
            lock.acquire()
            print(curr.value)
            curr.value += 1
            lock.release()


if __name__ == '__main__':
    num = multiprocessing.Value('i', 1)
    lock = multiprocessing.Lock()

    odd_process = multiprocessing.Process(target=odd, args=(num, 100, lock))
    even_process = multiprocessing.Process(target=even, args=(num, 100, lock))
    odd_process.start()
    even_process.start()
