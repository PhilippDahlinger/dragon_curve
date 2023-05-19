import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

from dragon_curve_gen import next_iteration, first_iteration
from rendering import print_curve, plot_curve


def plot_4_curves(d):
    fig, ax = plt.subplots()
    # plot_curve(ax, d, color="blue", start_dir=0)
    # plot_curve(ax, d, color="red", start_dir=1)
    # plot_curve(ax, d, color="green", start_dir=2)
    # plot_curve(ax, d, color="purple", start_dir=3)lue", start_dir=0)
    plot_curve(ax, d, color="all", start_dir=0)
    plot_curve(ax, d, color="all", start_dir=1)
    plot_curve(ax, d, color="all", start_dir=2)
    plot_curve(ax, d, color="all", start_dir=3)
    plt.show()
    plt.close()


if __name__ == '__main__':
    dragon_curves = [first_iteration()]
    for i in range(100):
        dragon_curves.append(next_iteration(dragon_curves[-1]))
        plot_4_curves(dragon_curves[-1])
    #
    # t = np.linspace(0, 10, 200)
    # x = np.cos(np.pi * t)
    # y = np.sin(t)
    #
    # # Create a set of line segments so that we can color them individually
    # # This creates the points as a N x 1 x 2 array so that we can stack points
    # # together easily to get the segments. The segments array for line collection
    # # needs to be numlines x points per line x 2 (x and y)
    # points = np.array([x, y]).T.reshape(-1, 1, 2)
    # segments = np.concatenate([points[:-1], points[1:]], axis=1)
    #
    # # Create the line collection object, setting the colormapping parameters.
    # # Have to set the actual values used for colormapping separately.
    # lc = LineCollection(segments, cmap=plt.get_cmap('copper'),
    #                     norm=plt.Normalize(0, 10))
    # lc.set_array(t)
    # lc.set_linewidth(3)
    #
    # plt.gca().add_collection(lc)
    # plt.xlim(-1, 1)
    # plt.ylim(-1, 1)
    # plt.show()

