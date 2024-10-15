from time import sleep

sleep(100)


def the_answer():
    import numpy as np

    large_array = np.ones((45_000_000,), dtype=np.float64)  # ~360MiB allocation
    array_sum = large_array[0] + large_array[1]
    result = array_sum + 40

    return result
