import threading

condition = threading.Condition()
start = 1
end = 100
curr = start


def odd():
    global curr, condition, end
    while True:
        condition.acquire()
        if curr >= end:
            condition.notifyAll()
            condition.release()
            break
        if not curr % 2:
            condition.wait()
        print(curr)
        curr += 1
        condition.notifyAll()
        condition.release()


def even():
    global curr, condition, end
    while True:
        condition.acquire()
        if curr >= end:
            condition.notifyAll()
            condition.release()
            break
        if curr % 2:
            condition.wait()
        print(curr)
        curr += 1
        condition.notifyAll()
        condition.release()


if __name__ == "__main__":
    thread_odd = threading.Thread(target=odd)
    thread_even = threading.Thread(target=even)
    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()
