
cpdef get_fibonacci(int n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    cdef int prev_prev = 1, prev = 0
    cdef curr = 0
    for _ in range(2, n):
        curr = prev + prev_prev
        prev_prev, prev = prev, curr
    return curr