import random

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap


def print_curve(d: np.array):
    result = ""
    for x in d:
        if x < 0:
            result += "L"
        else:
            result += "R"
    print(result)


def get_rotation_matrix(theta: float):
    """
    Returns 2d rotation matrix
    :param theta: in radians
    :return: 2d np array
    """
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))
    return R

def plot_curve(ax, d: np.array, angle_divisor: int = 4, start_dir: int = 0, start_pos: (float, float) = (0, 0),
               color="all"):
    iteration = int(np.round(np.log2(len(d) + 1)))
    ax.set_title(f"Iteration {iteration}, Length: {len(d)}")

    rotation_matrix = np.linalg.inv(get_rotation_matrix(2 * np.pi / angle_divisor))
    gen_dir_vector = np.array((0, 1))
    directions = []
    for angle in range(angle_divisor):
        directions.append(gen_dir_vector)
        gen_dir_vector = rotation_matrix @ gen_dir_vector
    # directions = [np.array((0, 1)), np.array((1, 0)), np.array((0, -1)), np.array((-1, 0))]
    half_rotation_matrix = get_rotation_matrix(np.pi / angle_divisor)
    powered_half_rotation_matrix = np.linalg.matrix_power(half_rotation_matrix, iteration)

    directions = [powered_half_rotation_matrix @ x for x in directions]

    current_dir = start_dir
    current_pos = np.array(start_pos) + directions[current_dir]
    #
    # x_list = [start_pos[0], current_pos[0]]
    # y_list = [start_pos[1], current_pos[1]]
    #
    # for fold in d:
    #     current_dir = (current_dir + fold) % angle_divisor
    #     current_pos += directions[current_dir]
    #     x_list.append(current_pos[0])
    #     y_list.append(current_pos[1])
    seqs = [((start_pos[0], start_pos[1]), (current_pos[0], current_pos[1]))]
    min_x, max_x = min(start_pos[0], current_pos[0]), max(start_pos[0], current_pos[0])
    min_y, max_y = min(start_pos[1], current_pos[1]), max(start_pos[1], current_pos[1])
    for fold in d:
        current_dir = (current_dir + fold) % angle_divisor
        new_pos = current_pos + directions[current_dir]
        seqs.append(((current_pos[0], current_pos[1]), (new_pos[0], new_pos[1])))

        current_pos = new_pos
        min_x, max_x = min(min_x, current_pos[0]), max(max_x, current_pos[0])
        min_y, max_y = min(min_y, current_pos[1]), max(max_y, current_pos[1])

    # Create LineCollection object
    if color == "all":
        lc = LineCollection(seqs, cmap=plt.get_cmap('viridis'),
                            norm=plt.Normalize(0, 10))
    else:
        lc = LineCollection(seqs, color=color,
                            norm=plt.Normalize(0, 10))
    lc.set_array(np.linspace(0, 10, len(d) + 1))
    # Add LineCollection to the plot
    ax.add_collection(lc)
    # update ax.viewLim using the new dataLim
    ax.autoscale_view(True, True, True)
    ax.set_aspect('equal', adjustable='box')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
