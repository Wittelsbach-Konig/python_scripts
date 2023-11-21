from typing import List
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f'Function {func.__name__!r} executed '
              f'in {time_end-time_start}s')
        return result
    return wrapper


def eratosphen(n: int) -> List[int]:
    numbers = list(range(n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


@execution_time
def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


@execution_time
def eratosphen_effective(n: int) -> List[int]:
    numbers = list(range(n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


if __name__ == "__main__":
    time_start = time.time()
    print(eratosphen(15))
    time_end = time.time()
    print(time_end-time_start)
    print(eratosphen_effective(1500))
    print(get_least_primes_linear(1500))
