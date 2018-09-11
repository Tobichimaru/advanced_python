import threading

event = threading.Event()
start = 1
end = 100
curr = start


def odd():
    global curr, event, end
    while True:
        event.clear()
        if curr >= end:
            break
        if curr % 2:
            event.wait()
        print(curr)
        curr += 1
        event.set()


def even():
    global curr, event, end
    while True:
        event.clear()
        if curr >= end:
            break
        if not curr % 2:
            event.wait()
        print(curr)
        curr += 1
        event.set()


if __name__ == "__main__":
    thread_odd = threading.Thread(target=odd)
    thread_even = threading.Thread(target=even)
    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()
