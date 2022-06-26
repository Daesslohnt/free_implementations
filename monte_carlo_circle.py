from time import perf_counter
import random
from numba import njit


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = perf_counter() * 1000
        val = func(*args, **kwargs)
        end = perf_counter() * 1000

        print(f'Time in seconds: {round((end - start), 4)}\nResult: {val}')

    return wrapper


@time_decorator
@njit
def monte_carlo(nruns: int) -> float:
    x, y = random.random(), random.random()
    suc = 0
    for _ in range(nruns):
        if x**2 + y**2 <= 0.5:
            suc += 1
    return suc / nruns

def main() -> None:
    runs = [10, 100, 1000, 100_000, 1_000_000]
    for nruns in runs:
        print(f'Nruns: {nruns}')
        monte_carlo(nruns)

if __name__ == '__main__':
    main()