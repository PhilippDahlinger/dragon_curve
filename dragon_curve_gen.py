from typing import List

import numpy as np


def first_iteration() -> np.array:
    return np.array([], dtype=np.int32)


def next_iteration(d_i: np.array) -> np.array:
    second_part = np.copy(d_i)[::-1] * -1
    return np.concatenate((d_i, np.array([1]), second_part))
