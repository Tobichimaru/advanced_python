import threading

lock = threading.Lock()
start = 1
end = 100
curr = start


def odd():
    global curr, lock, end
    while True:
        if curr % 2:
            lock.acquire()
            if curr > end:
                break
            print(curr)
            curr += 1
            lock.release()


def even():
    global curr, lock, end
    while True:
        if not curr % 2:
            lock.acquire()
            if curr > end:
                break
            print(curr)
            curr += 1
            lock.release()


if __name__ == "__main__":
    thread_odd = threading.Thread(target=odd)
    thread_even = threading.Thread(target=even)
    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()
