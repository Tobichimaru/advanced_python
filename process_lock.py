from multiprocessing import Process, Value, Lock


def odd(curr, end, lock):
    while True:
        if int(curr.value) % 2 == 1:
            lock.acquire()
            if curr.value > end:
                break
            print(curr.value)
            curr.value += 1
            lock.release()


def even(curr, end, lock):
    while True:
        if int(curr.value) % 2 == 0:
            lock.acquire()
            if curr.value > end:
                break
            print(curr.value)
            curr.value += 1
            lock.release()


if __name__ == '__main__':
    num = Value('i', 1)
    lock = Lock()

    odd_process = Process(target=odd, args=(num, 100, lock))
    even_process = Process(target=even, args=(num, 100, lock))
    odd_process.start()
    even_process.start()
    odd_process.join()
    even_process.join()
