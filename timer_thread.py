import threading

start = 1
end = 100
curr = start


def stub_func():
    pass


timer = threading.Timer(0.1, stub_func)


def odd():
    global curr, end
    while True:
        if curr >= end:
            break
        if curr % 2:
            continue
        print(curr)
        curr += 1


def even():
    global curr, end
    while True:
        if curr >= end:
            break
        if not curr % 2:
            continue
        print(curr)
        curr += 1


if __name__ == "__main__":
    threading.Timer(0.001, odd).start()
    threading.Timer(0.001, even).start()
