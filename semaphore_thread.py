import threading

semaphore = threading.Semaphore()
start = 1
end = 100
curr = start


def odd():
    global curr, semaphore, end
    while True:
        if curr % 2:
            semaphore.acquire()
            if curr > end:
                break
            print(curr)
            curr += 1
            semaphore.release()


def even():
    global curr, semaphore, end
    while True:
        if not curr % 2:
            semaphore.acquire()
            if curr > end:
                break
            print(curr)
            curr += 1
            semaphore.release()


if __name__ == "__main__":
    thread_odd = threading.Thread(target=odd)
    thread_even = threading.Thread(target=even)
    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()
