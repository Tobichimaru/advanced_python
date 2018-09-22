import aiohttp
import asyncio
import itertools
import random
import threading
import time
import urllib.request


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        print("{} {}".format(method.__name__, end - start))
        return result
    return timed


def write_to_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)


@asyncio.coroutine
def get(url):
    session = aiohttp.ClientSession()
    response = yield from session.get(url)
    session.close()
    return (yield from response.read())


@asyncio.coroutine
def download_file(url):
    content = yield from asyncio.async(get(url))
    file_string = "aiohttp_file_{}.html".format(random.randint(1, 1000))
    write_to_file(file_string, content)


@timeit
def aiohttp_get(urls):
    coroutines = [download_file(url) for url in urls]
    eloop = asyncio.get_event_loop()
    eloop.run_until_complete(asyncio.wait(coroutines))
    eloop.close()


def thread_fetch_page(url):
    url_handler = urllib.request.urlopen(url)
    content = url_handler.read()
    file_string = "thread_file_{}.html".format(random.randint(1, 1000))
    write_to_file(file_string, content)


@timeit
def thread_get(urls):
    threads = [threading.Thread(target=thread_fetch_page(url), args=(url,))
               for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    url = "https://scontent-frx5-1.xx.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/" \
          "25395974_188509598394665_1170163521227147635_n.jpg?" \
          "_nc_cat=107&oh=9a028c2c3614128bb176fba623a6e622&oe=5C25ADA7"
    urls = list(itertools.repeat(url, 10))
    aiohttp_get(urls)
    thread_get(urls)
