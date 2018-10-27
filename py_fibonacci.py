
def get_fibonacci(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    prev = 0
    prev_prev = 1
    for _ in range(n):
        curr = prev + prev_prev
        prev_prev, prev = prev, curr
    return curr
