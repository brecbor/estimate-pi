from random import random
import time
from multiprocessing import Pool


def simulate(n_points: int) -> int:
    inside = 0
    for _ in range(n_points):
        x = random()
        y = random()
        if x**2 + y**2 < 1:
            inside += 1
    return inside


def estimate_pi(n_points: int = 10**8, processes: int = 1) -> float:
    inside = 0
    with Pool(processes=processes) as pool:
        params = [n_points // 100] * 100

        for result in pool.imap_unordered(simulate, params):
            inside += result

    return 4.0 * inside / sum(params)


def main():
    for processes in [1, 4, 10, 20]:
        print(f"Processes: {processes}")
        start_time = time.time()
        print(estimate_pi(5 * 10**8, processes))
        end_time = time.time()
        print(f"Duration: {end_time - start_time}s\n")


if __name__ == "__main__":
    main()
