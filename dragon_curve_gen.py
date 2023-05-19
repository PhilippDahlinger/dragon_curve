from typing import List

import numpy as np


def first_iteration() -> np.array:
    return np.array([], dtype=np.int32)


def dragon_next_iteration(d_i: np.array) -> np.array:
    second_part = np.copy(d_i)[::-1] * -1
    return np.concatenate((d_i, np.array([1]), second_part))


def terdragon_next_iteration(d_i: np.array) -> np.array:
    d_i = list(d_i)
    result = [1, -1]
    for x in d_i:
        result += [x, 1, -1]
    return np.array(result)
