import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

from dragon_curve_gen import next_iteration, first_iteration
from rendering import print_curve, plot_curve


def plot_4_curves(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, color="blue", start_dir=0)
    plot_curve(ax, d, color="red", start_dir=1)
    plot_curve(ax, d, color="green", start_dir=2)
    plot_curve(ax, d, color="purple", start_dir=3)
    # plot_curve(ax, d, color="all", start_dir=0)
    # plot_curve(ax, d, color="all", start_dir=1)
    # plot_curve(ax, d, color="all", start_dir=2)
    # plot_curve(ax, d, color="all", start_dir=3)
    plt.show()
    plt.close()


def plot_single_curve(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, color="all", start_dir=1)
    plt.show()
    plt.close()

def animate_single_curve(d):
    plt.ion()
    plt.cla()
    plot_curve(plt.gca(), d, color="all", start_dir=1)
    plt.pause(1.0)





if __name__ == '__main__':
    dragon_curves = [first_iteration()]
    for i in range(20):
        dragon_curves.append(next_iteration(dragon_curves[-1]))
        plot_single_curve(dragon_curves[-1])
        # plot_4_curves(dragon_curves[-1])
        # animate_single_curve(dragon_curves[-1])




